#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error
import urllib.parse
import yaml
import concurrent.futures
import traceback
import argparse
import os

from urllib.parse import urljoin

from unist import *

LAYOUT_STYLE = {
    "display": "inline-block",
    "borderRadius": 8,
    "color": "white",
    "padding": 5,
    "margin": 5,
}

DEFAULT_STYLE = {"background": "#4E66F6", **LAYOUT_STYLE}

styles = {
    "domains": {"background": "#7A77B4", **LAYOUT_STYLE},
    "packages": {"background": "#B83BC0", **LAYOUT_STYLE},
}


def debug(data):
    if "PYTHIA_DEBUG" in os.environ:
        print(data, file=sys.stderr)
    return data


def fetch_yaml(url: str):
    print(f"Fetching {url}", file=sys.stderr, flush=True)
    with urllib.request.urlopen(url) as response:
        body = response.read().decode()
    return yaml.load(body, yaml.SafeLoader)


def parse_project_tags(tags: list[str]):
    """
    Parse a list of "domain:tag" MyST tags into a mapping of tags by domain.
    """
    tags_by_domain = {}
    for raw_tag in tags:
        try:
            domain, tag = raw_tag.split(":")
        except ValueError:
            continue

        domain_tags = tags_by_domain.setdefault(domain, [])
        domain_tags.append(tag)
    return tags_by_domain


def render_cookbook(name: str):
    try:
        print(f"Rendering {name}", file=sys.stderr, flush=True)
        raw_base_url = f"https://raw.githubusercontent.com/projectpythia/{name}/main/"
        config_url = urljoin(raw_base_url, "myst.yml")

        # Load JB data
        myst_config = fetch_yaml(config_url)
        project_config = myst_config["project"]
        title = project_config["title"]

        # Fetch gallery metadata            # Fall back on gallery
        try:
            gallery_config = fetch_yaml(urljoin(raw_base_url, "_gallery_info.yml"))
        except urllib.error.HTTPError as err:
            if err.code != 404:
                raise

            # Pull out MyST-supported metadata
            # TODO remove legacy _gallery_info config
            image_url = urljoin(raw_base_url, project_config["thumbnail"])
            tags = parse_project_tags(project_config["tags"])
        else:
            # Gallery and cookbook config files use same schema for gallery config
            image_url = urljoin(raw_base_url, gallery_config["thumbnail"])
            tags = gallery_config["tags"]

        book_url = urljoin("https://projectpythia.org", name)

        return debug(
            {
                "type": "card",
                "url": book_url,
                "children": [
                    {"type": "cardTitle", "children": [text(title)]},
                    div(
                        [
                            image(image_url),
                            div(
                                [
                                    span(
                                        [text(item)],
                                        style=styles.get(name, DEFAULT_STYLE),
                                    )
                                    for name, items in tags.items()
                                    if items is not None
                                    for item in items
                                ]
                            ),
                        ],
                    ),
                ],
            }
        )
    except Exception as err:
        print(f"\n\nError rendering {name}", file=sys.stderr)
        traceback.print_exception(err, file=sys.stderr)
        return None


def render_cookbooks(pool):
    with open("cookbook_gallery.txt") as f:
        body = f.read()

    return [c for c in pool.map(render_cookbook, body.splitlines()) if c is not None]


def run_directive(name, data):
    assert name == "pythia-cookbooks"
    return [{"type": "pythia-cookbooks", "children": []}]


def run_transform(name, data):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # Find our cookbook nodes in the AST
        cookbook_nodes = find_all_by_type(data, "pythia-cookbooks")

        # In-place mutate the AST to replace cookbook nodes with card grids
        children = render_cookbooks(pool)

        # Mutate our cookbook nodes in-place
        for node in cookbook_nodes:
            node.clear()
            node.update(grid([1, 1, 2, 3], children))
            node["children"] = children

    return data


pythiaGalleryDirective = {
    "name": "pythia-cookbooks",
    "doc": "An example directive for embedding a Pythia cookbook gallery.",
}
pythiaGalleryTransform = {
    "stage": "document",
}

PLUGIN_SPEC = {
    "name": "Pythia Gallery",
    "directives": [pythiaGalleryDirective],
    "transforms": [pythiaGalleryTransform],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        json.dump(run_directive(args.directive, data), sys.stdout)
    elif args.transform:
        data = json.load(sys.stdin)
        json.dump(run_transform(args.transform, data), sys.stdout)
    elif args.role:
        raise NotImplementedError
    else:
        json.dump(PLUGIN_SPEC, sys.stdout)
