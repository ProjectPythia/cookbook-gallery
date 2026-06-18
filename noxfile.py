"""Developer tasks. Run `nox -l` to list sessions."""

import nox


@nox.session(name="docs", venv_backend="none")
def docs(session):
    """Build the static site into docs/_build/html (used locally and in CI)."""
    session.chdir("docs")
    session.run("myst", "build", "--html", external=True)


@nox.session(name="docs-live", venv_backend="none")
def docs_live(session):
    """Live-preview the docs/ site with hot reload at http://localhost:3000.

    Needs `myst` on PATH (e.g. `npm install -g mystmd`, or the conda env).
    """
    session.chdir("docs")
    session.run("myst", "start", external=True)
