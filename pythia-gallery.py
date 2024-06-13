import sys
import json
import urllib.request
import yaml
import concurrent.futures

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
    with urllib.request.urlopen(url) as response:
        body = response.read().decode()
    return yaml.load(body, yaml.SafeLoader)


def render_cookbook(name: str):
    raw_base_url = f"https://raw.githubusercontent.com/ProjectPythia-MystMD/{name}/main"
    base_url = f"https://github.com/ProjectPythia-MystMD/{name}"
    config_url = f"{raw_base_url}/_config.yml"
    book_url = f"https://projectpythia.org/{name}"

    # Load JB data
    data = fetch_yaml(config_url)
    title = data["title"]

    # Fetch gallery metadata
    gallery_url = f"{raw_base_url}/_gallery_info.yml"
    gallery_data = fetch_yaml(gallery_url)
    image_name = gallery_data["thumbnail"]
    image_url = f"{raw_base_url}/{image_name}"

    # Build tags
    tags = gallery_data["tags"]

    return {
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


def render_cookbooks(pool):
    with open("cookbook_gallery.txt") as f:
        body = f.read()

    return [*pool.map(render_cookbook, body.splitlines())]


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # Parse the AST as JSON on stdin
        data = sys.stdin.read()
        ast = json.loads(data)

        # Find our cookbook nodes in the AST
        cookbook_nodes = find_all_by_type(ast, "pythia-cookbooks")

        # In-place mutate the AST to replace cookbook nodes with card grids
        children = render_cookbooks(pool)

        # Mutate our cookbook nodes in-place
        for node in cookbook_nodes:
            node.clear()
            node.update(grid([1, 1, 2, 3], children))
            node["children"] = children

        # Write back to stdout!
        print(json.dumps(ast))
