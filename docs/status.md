(nightly-build-status)=
# Cookbook build status

Every cookbook is rebuilt nightly. This table tracks each book's health.
Click a cookbook to open its workflow runs on GitHub.[^fn]

:::{listing}
:source: pythia-status
:display: table
:columns: title,build,updated
:sort: title
:limit: 100
:::


[^fn]: Each status comes from the repo's nightly workflow badge, and the updated date is the book's last successful deploy.
  A book with no deploy in the last week is "⚠️ no longer updating" whatever its badge says, since a disabled workflow keeps serving its last badge.
  A ❌ means the nightly build fails but pushes still deploy the book.
  Everything is only as fresh as the last build of [this gallery](./developing.md).
