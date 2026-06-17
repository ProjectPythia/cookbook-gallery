# Developer documentation

How the [gallery](./index.md) is built, and how to add your own cookbook to it.

The gallery is a thin **collector** for the
[`myst-listing`](https://github.com/myst-contrib/myst-listing)
plugin: we fetch the cookbook metadata, myst-listing renders the cards, and
[`searchfilter`](https://github.com/jupyter-book/myst-plugins/tree/main/plugins/searchfilter)
adds a live filter box.

The **list of repositories to use in the gallery** is in the `cookbook_gallery.txt` file.

## Add a cookbook

Each card in the gallery is assembled from two files in each cookbook's repo.

1. **List the repo.**
Add its repository name (one per line) to [`cookbook_gallery.txt`](../cookbook_gallery.txt) at the root of this repo.

2. **Describe the card.**
Add a `_gallery_info.yml` to the root of your cookbook repo:

   ```yaml
   thumbnail: thumbnail.png        # path to an image in your repo
   tags:
     domains: [oceanography, climate]
     packages: [xarray, dask]
   ```

That's it.
The card's **title** comes from your cookbook's `myst.yml` (`project.title`), and the **description** from your `CITATION.cff` `abstract` — so you don't repeat them here.

### What ends up on the card

| Card field | Source |
|------------|--------|
| Title | `myst.yml` → `project.title` |
| Description | `CITATION.cff` → `abstract` (or `myst.yml` `project.description` if set) |
| Thumbnail | `_gallery_info.yml` → `thumbnail` |
| Tags | `_gallery_info.yml` → `tags` (each category becomes a colored pill group) |
| Link | `https://projectpythia.org/<repo-name>` |

Each tag category (`domains`, `packages`, `events`) is passed through as its own
item field, and the listing's `:tag-fields: domains,packages,events` renders each
as a separately-colored group of pills. Add a category to that list to show it.

## How it works

1. `{listing}` (from myst-listing) with `:source: pythia` emits a `listingPlaceholder` node.
2. Our document-stage transform in `src/pythia_gallery.py` finds those nodes and fills each one's `items` — one entry per cookbook, fetched in parallel from the repos in [`cookbook_gallery.txt`](../cookbook_gallery.txt).
3. myst-listing renders the items as a gallery grid, and `{searchfilter}` filters the cards client-side.

So `src/pythia_gallery.py` is **only** a collector: it never defines a directive or renders anything.
`:source: pythia` plugs straight into the standard `{listing}` directive and all its options, and myst-listing's own collector ignores our source — so there's no conflict.

`{searchfilter}` targets `.myst-listing-gallery .myst-card` (not `.myst-listing-item`) because the gallery's `card` nodes drop custom classes.

## Preview locally

The whole site lives in `docs/`. Live-preview it with hot reload:

```bash
nox -s docs-live      # serves the gallery + these docs at http://localhost:3000
```

`nox -s docs-live` just runs `myst start` inside `docs/`, so you need `myst` on
your PATH (`npm install -g mystmd`, or the project conda env). No nox session?
`cd docs && myst start` does the same thing.

## The plugins

`docs/myst.yml` loads both plugins from their GitHub releases — single built
bundles, no local checkout or build step:

```yaml
- https://github.com/myst-contrib/myst-listing/releases/download/v0.1.0/plugin.mjs
- https://raw.githubusercontent.com/jupyter-book/myst-plugins/main/plugins/searchfilter/searchfilter.mjs
```

myst-listing is pinned to `v0.1.0`; to track the newest release instead, swap
the tag for `latest/download`. Because both are fetched from URLs, the site
builds anywhere — CI and fresh clones included.
