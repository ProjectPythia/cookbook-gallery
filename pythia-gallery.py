#!/usr/bin/env python3
import sys
import json
import urllib.request
import yaml
import concurrent.futures
import traceback
import argparse

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


def fetch_yaml(url: str):
    print(f"Fetching {url}", file=sys.stderr, flush=True)
    with urllib.request.urlopen(url) as response:
        body = response.read().decode()
    return yaml.load(body, yaml.SafeLoader)


def fetch_cookbook_data(name):
    """Fetch and return cookbook metadata from myst.yml and _gallery_info.yml."""
    try:
        print(f"Fetching metadata for {name}", file=sys.stderr, flush=True)
        raw_base_url = f"https://raw.githubusercontent.com/ProjectPythia-MystMD/{name}/main"

        # Load myst.yml
        config_url = f"{raw_base_url}/myst.yml"
        config = fetch_yaml(config_url)
        title = config["project"]["title"]

        # Load _gallery_info.yml
        gallery_url = f"{raw_base_url}/_gallery_info.yml"
        gallery_data = fetch_yaml(gallery_url)

        # Extract image details and tags
        image_url = f"{raw_base_url}/{gallery_data['thumbnail']}"
        tags = gallery_data.get("tags", {})

        return {
            "title": title,
            "book_url": f"https://projectpythia-mystmd.github.io/{name}",
            "image_url": image_url,
            "tags": tags,  # Dictionary of {"domains": [...], "packages": [...]}
        }

    except Exception as err:
        print(f"Error fetching data for {name}", file=sys.stderr)
        traceback.print_exception(err, file=sys.stderr)
        return None


def render_cookbook(name, data):
    """Render a cookbook card from fetched metadata."""
    try:
        print(f"Rendering {name}", file=sys.stderr, flush=True)
        return {
            "type": "card",
            "url": data["book_url"],
            "class": ["tagged-card"] + [item for _, items in data["tags"].items() for item in items],
            "children": [
                {"type": "cardTitle", "children": [text(data["title"])]},
                div(
                    [
                        image(data["image_url"]),
                        div(
                            [
                                span(
                                    [text(item)],
                                    style=styles.get(category, DEFAULT_STYLE),
                                )
                                for category, items in data["tags"].items() if items
                                for item in items
                            ]
                        ),
                    ],
                ),
            ],
        }
    except Exception as err:
        print(f"\n\nError rendering {name}", file=sys.stderr)
        traceback.print_exception(err, file=sys.stderr)
        return None


def render_cookbooks(pool):
    with open("cookbook_gallery.txt") as f:
        body = f.read().splitlines()

    # Fetch all cookbook data in parallel
    cookbook_entries = list(pool.map(fetch_cookbook_data, body))

    cookbook_data = {}
    tag_lists = {"domains": set(), "packages": set()}

    for name, data in zip(body, cookbook_entries):
        if data:
            cookbook_data[name] = render_cookbook(name, data)  # Use pre-fetched data
            
            # Collect tags into tag_lists
            for category in tag_lists.keys():
                tag_lists[category].update(data["tags"].get(category, []))

    # Create dropdown HTML
    dropdown_html = f"""
    <div class="dropdown-container">
        <label for="domain-dropdown">Filter by Domain</label>
        <select id="domain-dropdown">
            <option value="">All</option>
            {"".join([f'<option value="{tag}">{tag}</option>' for tag in sorted(tag_lists["domains"])])}
        </select>

        <label for="package-dropdown">Filter by Package</label>
        <select id="package-dropdown">
            <option value="">All</option>
            {"".join([f'<option value="{tag}">{tag}</option>' for tag in sorted(tag_lists["packages"])])}
        </select>
    </div>
    """

    return dropdown_html, cookbook_data, {key: sorted(value) for key, value in tag_lists.items()}


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
