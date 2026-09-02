#!/usr/bin/env python3
"""Pythia gallery: `pythia` sources for the myst-listing plugin.

Use `:::{listing}` with `:source: pythia` (the gallery cards) or
`:source: pythia-status` (the build status table). Our document-stage
transform fills any such placeholder's `items` with one entry per cookbook;
myst-listing then renders them. See docs/developing.md.
"""
import sys
import datetime
import json
import re
import urllib.request
import yaml
import concurrent.futures
import traceback
import argparse
import pathlib

PLACEHOLDER = "listingPlaceholder"  # myst-listing's node type
# Resolve the repo-root list relative to this file, not the current directory,
# so the plugin works whether myst runs from the repo root or from docs/.
COOKBOOKS = pathlib.Path(__file__).resolve().parent.parent / "cookbook_gallery.txt"
# Collected metadata is cached here, under the site's _build/ (CWD is the
# project root). Keeps rebuilds from re-fetching every repo every time.
CACHE = pathlib.Path("_build") / "pythia-gallery.json"


def fetch_text(url):
    print(f"Fetching {url}", file=sys.stderr, flush=True)
    # timeout so one stalled host can't hang the whole build forever.
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode()


def fetch_yaml(url):
    return yaml.load(fetch_text(url), yaml.SafeLoader)


def fetch_abstract(name, raw):
    """The cookbook's CITATION.cff abstract, or None if missing/unreadable.

    A failure here just means no description; it never drops the cookbook.
    """
    try:
        return fetch_yaml(f"{raw}/CITATION.cff").get("abstract")
    except Exception as err:
        print(f"  no CITATION.cff abstract for {name}: {err}", file=sys.stderr)
        return None


def fetch_build_status(name):
    """The cookbook's nightly build status ("✅ passing"/"❌ failing"), or None.

    Parsed from the Actions badge SVG, which embeds the status as text and
    needs no auth or API rate limit. "no status" (workflow disabled or never
    run) and fetch errors both mean None: a blank cell in the status table.
    """
    url = f"https://github.com/ProjectPythia/{name}/actions/workflows/nightly-build.yaml/badge.svg"
    try:
        svg = fetch_text(url)
        for status, mark in (("passing", "✅"), ("failing", "❌")):
            if status in svg:
                return f"{mark} {status}"
    except Exception as err:
        print(f"  no nightly badge for {name}: {err}", file=sys.stderr)
    return None


def fetch_deploy_date(name):
    """The date ("YYYY-MM-DD") the cookbook's book was last deployed, or None.

    Read from the public Atom feed of the repo's gh-pages branch (its newest
    commit is the last successful deploy), so no API token is needed.
    """
    url = f"https://github.com/ProjectPythia/{name}/commits/gh-pages.atom"
    try:
        match = re.search(r"<updated>(\d{4}-\d{2}-\d{2})", fetch_text(url))
        return match and match.group(1)
    except Exception as err:
        print(f"  no gh-pages feed for {name}: {err}", file=sys.stderr)
        return None


def collect_cookbook(name):
    """Fetch one cookbook's metadata as a myst-listing item (or None on error)."""
    try:
        raw = f"https://raw.githubusercontent.com/projectpythia/{name}/main"
        project = fetch_yaml(f"{raw}/myst.yml")["project"]
        gallery = fetch_yaml(f"{raw}/_gallery_info.yml")
        status = fetch_build_status(name)
        updated = fetch_deploy_date(name)
        # A book that has stopped deploying is not working.
        # A disabled workflow keeps serving its last (stale) badge.
        # The week of grace forgives transient CI outages between nightlies.
        week_ago = datetime.date.today() - datetime.timedelta(days=7)
        if updated is None or datetime.date.fromisoformat(updated) < week_ago:
            status = "⚠️ no longer updating"
        return {
            # Tag categories (domains/packages/events) pass through as their own
            # fields so myst-listing's :tag-fields: renders each as a colored
            # group. Spread first, so our explicit fields below always win.
            **(gallery.get("tags") or {}),
            # For the status table; not shown on the gallery cards.
            "build": status,
            "updated": updated,
            "name": name,
            "title": project["title"],
            # The cookbook's own description if set, else its CITATION.cff abstract.
            "description": project.get("description") or fetch_abstract(name, raw),
            "thumbnail": f"{raw}/{gallery['thumbnail']}",
            "url": f"https://projectpythia.org/{name}",
        }
    except Exception as err:
        print(f"\n\nError collecting {name}: {err}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def collect_cookbooks():
    # Reuse the cache until cookbook_gallery.txt changes; delete _build (or that
    # file) to force a full refresh. CI starts from a clean _build, so it always
    # fetches fresh.
    if CACHE.is_file() and CACHE.stat().st_mtime >= COOKBOOKS.stat().st_mtime:
        return json.loads(CACHE.read_text())
    with open(COOKBOOKS) as f:
        names = f.read().splitlines()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        items = [c for c in pool.map(collect_cookbook, names) if c is not None]
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(items))
    return items


def status_items(items):
    """Rows for `:source: pythia-status`: the title links to the nightly workflow."""
    return [
        {
            "title": item["title"],
            "build": item.get("build"),
            "updated": item.get("updated"),
            "url": f"https://github.com/ProjectPythia/{item['name']}"
            "/actions/workflows/nightly-build.yaml",
        }
        for item in items
    ]


def find_all_by_type(parent, type_):
    for node in parent.get("children", []):
        if node.get("type") == type_:
            yield node
        yield from find_all_by_type(node, type_)


def run_transform(data):
    nodes = [
        node
        for node in find_all_by_type(data, PLACEHOLDER)
        if node.get("source") in ("pythia", "pythia-status")
    ]
    if nodes:
        items = collect_cookbooks()
        for node in nodes:
            node["items"] = (
                status_items(items) if node["source"] == "pythia-status" else items
            )
    return data


PLUGIN_SPEC = {
    "name": "Pythia Gallery",
    "transforms": [{"stage": "document"}],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--transform")
    args = parser.parse_args()

    if args.transform:
        json.dump(run_transform(json.load(sys.stdin)), sys.stdout)
    else:
        json.dump(PLUGIN_SPEC, sys.stdout)
