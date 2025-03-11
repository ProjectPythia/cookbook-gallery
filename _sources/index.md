
# Cookbooks Gallery


Pythia Cookbooks provide example workflows on more advanced and domain-specific problems developed by the Pythia community. Cookbooks build on top of skills you learn in [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html).

Cookbooks are created from Jupyter Notebooks that we strive to binderize so each Cookbook can be [executed in the cloud with a single click from your browser](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-notebooks-in-the-cloud-via-binder), but in some instances executing a Cookbook will require [running the notebooks locally](https://foundations.projectpythia.org/preamble/how-to-use.html#interacting-with-jupyter-books-locally).

Interested in contributing a new Cookbook or contributing to an existing Cookbook? Great! Please see the [Project Pythia Cookbook Contributor's Guide](https://projectpythia.org/cookbook-guide.html), and consider opening a discussion under the [Project Pythia category of the Pangeo Discourse](https://discourse.pangeo.io/c/education/project-pythia/60).

<div class="d-sm-flex mt-3 mb-4">
<div class="d-flex gallery-menu">
<div><a role="button" class="btn btn-primary btn-sm mx-1" href=https://projectpythia.org/cookbook-guide.html>How can I create a new Cookbook?</a></div>
</div>
<div class="ml-auto d-flex">
<div><button class="btn btn-link btn-sm mx-1" onclick="clearCbs()">Clear all filters</button></div>

:::{dropdown} domains
<div class="dropdown">
<ul>
<li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=d-visualizations onchange="change();">&nbsp;3D Visualizations</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=aws-cloud onchange="change();">&nbsp;AWS Cloud</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=atmosphere onchange="change();">&nbsp;Atmosphere</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=basemaps onchange="change();">&nbsp;Basemaps</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate onchange="change();">&nbsp;Climate</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate-model onchange="change();">&nbsp;Climate Model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=climate-modeling onchange="change();">&nbsp;Climate Modeling</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-access onchange="change();">&nbsp;Data Access</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=data-science onchange="change();">&nbsp;Data Science</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=earth-observation onchange="change();">&nbsp;Earth-Observation</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=fourier-transform onchange="change();">&nbsp;Fourier Transform</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=gis onchange="change();">&nbsp;GIS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=geospatial onchange="change();">&nbsp;Geospatial</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=geospatial-data onchange="change();">&nbsp;Geospatial Data</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=hrrr-model onchange="change();">&nbsp;HRRR Model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=intake onchange="change();">&nbsp;Intake</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=interactive-visualization onchange="change();">&nbsp;Interactive-Visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=land-model onchange="change();">&nbsp;Land Model</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=machine-learning onchange="change();">&nbsp;Machine Learning</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=meteorology onchange="change();">&nbsp;Meteorology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=microwave-remote-sensing onchange="change();">&nbsp;Microwave-Remote-Sensing</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=ml onchange="change();">&nbsp;Ml</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=nasa-earthdata-gibs onchange="change();">&nbsp;NASA EarthData GIBS</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=nsf-jetstream2 onchange="change();">&nbsp;NSF JetStream2</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=oceanography onchange="change();">&nbsp;Oceanography</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=paleoclimatology onchange="change();">&nbsp;Paleoclimatology</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=particles onchange="change();">&nbsp;Particles</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=radar onchange="change();">&nbsp;Radar</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=remote-sensing onchange="change();">&nbsp;Remote-Sensing</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=satellite onchange="change();">&nbsp;Satellite</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=satellite-imagery onchange="change();">&nbsp;Satellite Imagery</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=scientific-software-engineering onchange="change();">&nbsp;Scientific Software Engineering</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sentinel-1 onchange="change();">&nbsp;Sentinel-1</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sentinel-2 onchange="change();">&nbsp;Sentinel-2</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=signal-analysis onchange="change();">&nbsp;Signal Analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=spatial-analysis onchange="change();">&nbsp;Spatial Analysis</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=stac onchange="change();">&nbsp;Stac</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=sustainability onchange="change();">&nbsp;Sustainability</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=visualization onchange="change();">&nbsp;Visualization</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=wavelet onchange="change();">&nbsp;Wavelet</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=weather onchange="change();">&nbsp;Weather</label></li><li><label class="dropdown-item checkbox domains"><input type="checkbox" rel=zarr onchange="change();">&nbsp;Zarr</label></li>
</ul>
</div>
:::


:::{dropdown} events
<div class="dropdown">
<ul>
<li><label class="dropdown-item checkbox events"><input type="checkbox" rel=cook-off-2023 onchange="change();">&nbsp;Cook-Off 2023</label></li><li><label class="dropdown-item checkbox events"><input type="checkbox" rel=cook-off-2024 onchange="change();">&nbsp;Cook-Off 2024</label></li>
</ul>
</div>
:::


:::{dropdown} packages
<div class="dropdown">
<ul>
<li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=cartopy onchange="change();">&nbsp;Cartopy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=dask onchange="change();">&nbsp;Dask</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=datashader onchange="change();">&nbsp;Datashader</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=eofs onchange="change();">&nbsp;Eofs</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geocat-datafiles onchange="change();">&nbsp;Geocat-Datafiles</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geocat-viz onchange="change();">&nbsp;Geocat-Viz</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=geoviews onchange="change();">&nbsp;Geoviews</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=holoviews onchange="change();">&nbsp;Holoviews</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=hvplot onchange="change();">&nbsp;HvPlot</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=hvplot onchange="change();">&nbsp;Hvplot</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=ipython onchange="change();">&nbsp;IPython</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake onchange="change();">&nbsp;Intake</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-esgf onchange="change();">&nbsp;Intake-Esgf</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-esm onchange="change();">&nbsp;Intake-Esm</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-markdown onchange="change();">&nbsp;Intake-Markdown</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=intake-xarray onchange="change();">&nbsp;Intake-Xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=kerchunk onchange="change();">&nbsp;Kerchunk</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=matplotlib onchange="change();">&nbsp;Matplotlib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=metpy onchange="change();">&nbsp;Metpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=numpy onchange="change();">&nbsp;Numpy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=odc-stac onchange="change();">&nbsp;Odc-Stac</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=odc.stac onchange="change();">&nbsp;Odc.Stac</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=owslib onchange="change();">&nbsp;Owslib</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pandas onchange="change();">&nbsp;Pandas</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=panel onchange="change();">&nbsp;Panel</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=planetary-computer onchange="change();">&nbsp;Planetary-Computer</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=py-art onchange="change();">&nbsp;Py-Art</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pyleoclim onchange="change();">&nbsp;Pyleoclim</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pyresample onchange="change();">&nbsp;Pyresample</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pystac-client onchange="change();">&nbsp;Pystac-Client</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=pywavelets onchange="change();">&nbsp;Pywavelets</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=rioxarray onchange="change();">&nbsp;Rioxarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=scipy onchange="change();">&nbsp;Scipy</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=seaborn onchange="change();">&nbsp;Seaborn</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=tensorflow onchange="change();">&nbsp;Tensorflow</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=vapor onchange="change();">&nbsp;Vapor</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=verde onchange="change();">&nbsp;Verde</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xesmf onchange="change();">&nbsp;XESMF</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xarray onchange="change();">&nbsp;Xarray</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xbatcher onchange="change();">&nbsp;Xbatcher</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xeofs onchange="change();">&nbsp;Xeofs</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xesmf onchange="change();">&nbsp;Xesmf</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=xradar onchange="change();">&nbsp;Xradar</label></li><li><label class="dropdown-item checkbox packages"><input type="checkbox" rel=zarr onchange="change();">&nbsp;Zarr</label></li>
</ul>
</div>
:::

</div>
</div>
<script>$(document).on("click",function(){$(".collapse").collapse("hide");}); </script>


::::{grid} 1
:gutter: 0


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card climate dask intake-esm xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/cesm-lens-aws-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/cesm-lens-aws-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">CESM LENS on AWS Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Anderson Banihirwe, Brian Bonnlander, Jeff de La Beaujardière, Scott Henderson, CESM LENS on AWS Cookbook contributors</p>
<p class="my-2">Notebooks developed to demonstrate analysis of CESM LENS data publicly available on Amazon S3 (us-west-2 region) using Xarray and Dask. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Dask</span>
<span class="badge bg-primary mybadges">Intake-Esm</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/cesm-lens-aws-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/cesm-lens-aws-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/cesm-lens-aws-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/509240024"><img alt="DOI" src="https://zenodo.org/badge/509240024.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card climate intake-esm xesmf

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/cmip6-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/cmip6-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">CMIP6 Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Ryan Abernathey, Henri Drake, Robert R. Ford, CMIP6 Cookbook contributors</p>
<p class="my-2">Examples of analysis of Google Cloud CMIP6 data using Pangeo tools. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Intake-Esm</span>
<span class="badge bg-primary mybadges">Xesmf</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/cmip6-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/cmip6-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/cmip6-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/507993770"><img alt="DOI" src="https://zenodo.org/badge/507993770.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card AWS-cloud HRRR-model xarray zarr

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/HRRR-AWS-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/HRRR-AWS-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">HRRR AWS Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Kevin Tyle, HRRR-AWS Cookbook contributors</p>
<p class="my-2">A cookbook for working with AWS-served HRRR model output data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">AWS-Cloud</span>
<span class="badge bg-primary mybadges">HRRR-Model</span>
<span class="badge bg-primary mybadges">Xarray</span>
<span class="badge bg-primary mybadges">Zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/HRRR-AWS-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/HRRR-AWS-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/507993773"><img alt="DOI" src="https://zenodo.org/badge/507993773.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2023 Cook-off-2024 Py-Art Xradar atmosphere radar

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/radar-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/radar-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Radar Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Maxwell Grover, Zachary Sherman, Milind Sharma, Alfonso Ladino, Crystal Camron, Takashi Unuma, Radar Cookbook contributors</p>
<p class="my-2">A cookbook meant to work with various weather radar data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2023</span>
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Py-Art</span>
<span class="badge bg-primary mybadges">Xradar</span>
<span class="badge bg-primary mybadges">Atmosphere</span>
<span class="badge bg-primary mybadges">Radar</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/radar-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/radar-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/radar-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/479066261"><img alt="DOI" src="https://zenodo.org/badge/479066261.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Data-access intake intake-markdown intake-xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/intake-cookbook/main/thumbnail.svg" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/intake-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Intake Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> James Morley, Intake Cookbook contributors</p>
<p class="my-2">This cookbook shows examples of using and creating Intake catalogs to access data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Data-Access</span>
<span class="badge bg-primary mybadges">Intake</span>
<span class="badge bg-primary mybadges">Intake-Markdown</span>
<span class="badge bg-primary mybadges">Intake-Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/intake-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/intake-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/intake-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/512825541"><img alt="DOI" src="https://zenodo.org/badge/512825541.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card climate dask hvPlot intake ml satellite xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/landsat-ml-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/landsat-ml-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Landsat ML Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Demetris Roumis, Landsat ML Cookbook contributors</p>
<p class="my-2">Machine learning on Landsat data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Dask</span>
<span class="badge bg-primary mybadges">HvPlot</span>
<span class="badge bg-primary mybadges">Intake</span>
<span class="badge bg-primary mybadges">Ml</span>
<span class="badge bg-primary mybadges">Satellite</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/landsat-ml-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/landsat-ml-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/landsat-ml-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/563445694"><img alt="DOI" src="https://zenodo.org/badge/563445694.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card AWS-Cloud Data-Access HRRR-model intake kerchunk xarray zarr

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/kerchunk-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/kerchunk-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Kerchunk Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Norland Raphael Hagen, Kerchunk Cookbook contributors</p>
<p class="my-2">Kerchunk provides cloud-friendly access to archival data. With Kerchunk you can read collections of legacy file formats (NetCDF, GRIB2 etc.) as if they were ARCO (Analysis-Ready Cloud-Optimized) formats such as Zarr, without creating a copy of the original dataset. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">AWS-Cloud</span>
<span class="badge bg-primary mybadges">Data-Access</span>
<span class="badge bg-primary mybadges">HRRR-Model</span>
<span class="badge bg-primary mybadges">Intake</span>
<span class="badge bg-primary mybadges">Kerchunk</span>
<span class="badge bg-primary mybadges">Xarray</span>
<span class="badge bg-primary mybadges">Zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/kerchunk-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/kerchunk-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/kerchunk-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/588661659"><img alt="DOI" src="https://zenodo.org/badge/588661659.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card IPython data-science intake machine-learning matplotlib numpy oceanography scientific-software-engineering tensorflow xarray xbatcher zarr

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/xbatcher-ML-1-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/xbatcher-ML-1-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">xbatcher for Machine Learning Part 1 Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Christopher Dupuis, Anirban Sinha, Ryan Abernathey, xbatcher for Machine Learning Part 1 Cookbook contributors</p>
<p class="my-2">A complete workflow for a convolutional neural network using xbatcher. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">IPython</span>
<span class="badge bg-primary mybadges">Data-Science</span>
<span class="badge bg-primary mybadges">Intake</span>
<span class="badge bg-primary mybadges">Machine-Learning</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Numpy</span>
<span class="badge bg-primary mybadges">Oceanography</span>
<span class="badge bg-primary mybadges">Scientific-Software-Engineering</span>
<span class="badge bg-primary mybadges">Tensorflow</span>
<span class="badge bg-primary mybadges">Xarray</span>
<span class="badge bg-primary mybadges">Xbatcher</span>
<span class="badge bg-primary mybadges">Zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/xbatcher-ML-1-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/xbatcher-ML-1-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/xbatcher-ML-1-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/597998597"><img alt="DOI" src="https://zenodo.org/badge/597998597.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card dask xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/dask-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/dask-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Dask Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Negin Sobhani, Vanderwende Brian, Deepak Cherian, Ben Kirk, Dask Cookbook contributors</p>
<p class="my-2">A cookbook for Dask workflows. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Dask</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/dask-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/dask-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="http://binder.projectpythia.org/v2/gh/ProjectPythia/dask-cookbook.git/main"><img alt="Binder" src="http://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/610934658"><img alt="DOI" src="https://zenodo.org/badge/610934658.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2023 Cook-off-2024 geoviews meteorology panel xarray zarr

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/ERA5_interactive-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/ERA5_interactive-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">ARCO ERA-5 Interactive Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Kevin Tyle, Michael Barletta, ARCO ERA-5 Cookbook contributors</p>
<p class="my-2">A cookbook to interactively explore and visualize ERA-5 data in ARCO format. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2023</span>
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Geoviews</span>
<span class="badge bg-primary mybadges">Meteorology</span>
<span class="badge bg-primary mybadges">Panel</span>
<span class="badge bg-primary mybadges">Xarray</span>
<span class="badge bg-primary mybadges">Zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/ERA5_interactive-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/ERA5_interactive-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/ERA5_interactive-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/657280462"><img alt="DOI" src="https://zenodo.org/badge/657280462.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Basemaps GIS Geospatial-data NASA-EarthData-GIBS Satellite-imagery Spatial-analysis cartopy geoviews hvPlot owslib panel

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/web-map-feature-services-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/web-map-feature-services-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Web Map / Feature Services Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Andrew Huang, Web Map / Feature Services Cookbook contributors</p>
<p class="my-2">Learn how to use web map and feature services to easily and quickly provide spatial context, without the need to download and process GBs of data! </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Basemaps</span>
<span class="badge bg-primary mybadges">GIS</span>
<span class="badge bg-primary mybadges">Geospatial-Data</span>
<span class="badge bg-primary mybadges">NASA-EarthData-GIBS</span>
<span class="badge bg-primary mybadges">Satellite-Imagery</span>
<span class="badge bg-primary mybadges">Spatial-Analysis</span>
<span class="badge bg-primary mybadges">Cartopy</span>
<span class="badge bg-primary mybadges">Geoviews</span>
<span class="badge bg-primary mybadges">HvPlot</span>
<span class="badge bg-primary mybadges">Owslib</span>
<span class="badge bg-primary mybadges">Panel</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/web-map-feature-services-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/web-map-feature-services-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/web-map-feature-services-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/653301659"><img alt="DOI" src="https://zenodo.org/badge/653301659.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card dask geoviews hvplot interactive-visualization odc.stac panel planetary-computer satellite sentinel-2 xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/interactive-sentinel-2-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/interactive-sentinel-2-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Sentinel-2 L2A Interactive Dashboard</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Pritam Das, This Cookbook contributors</p>
<p class="my-2">This Project Pythia Cookbook provides a recipe for building an interactive dashboard for the Sentinel-2 L2A satellite imagery using the holoviews ecosystem. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Dask</span>
<span class="badge bg-primary mybadges">Geoviews</span>
<span class="badge bg-primary mybadges">Hvplot</span>
<span class="badge bg-primary mybadges">Interactive-Visualization</span>
<span class="badge bg-primary mybadges">Odc.Stac</span>
<span class="badge bg-primary mybadges">Panel</span>
<span class="badge bg-primary mybadges">Planetary-Computer</span>
<span class="badge bg-primary mybadges">Satellite</span>
<span class="badge bg-primary mybadges">Sentinel-2</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/interactive-sentinel-2-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/656355201"><img alt="DOI" src="https://zenodo.org/badge/656355201.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Pyresample verde xESMF xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/gridding-cookbook/main/grid_thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/gridding-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">(re)Gridding with xarray</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Thomas Martin, (re)Gridding with xarray contributors</p>
<p class="my-2">A small collection of notebooks that explores some (re)gridding options within the Xarray ecosystem. The thumbnail image was created with the assistance of DALL·E 2. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Pyresample</span>
<span class="badge bg-primary mybadges">Verde</span>
<span class="badge bg-primary mybadges">XESMF</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/gridding-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/gridding-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/540167581"><img alt="DOI" src="https://zenodo.org/badge/540167581.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card 3D-visualizations climate numpy particles vapor weather xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/vapor-python-cookbook/main/vapor_thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/vapor-python-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Vapor Python Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Nihanth Cherukuru, Stanislaw 'Stas' Jarosynski, Philip Austin, VAPOR python cookbook contributors</p>
<p class="my-2">The Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers (VAPOR) provides an interactive 3D visualization environment for exploratory visual analysis and the production of captivating animations and high-quality images. VAPOR runs on most UNIX and Windows systems equipped<a class="modal-btn"> ... more</a> </p>
</div>
</div>

<div class="modal">
<div class="content">
<img src="https://raw.githubusercontent.com/ProjectPythia/vapor-python-cookbook/main/vapor_thumbnail.png" class="modal-img" />
<h3 class="display-3">Vapor Python Cookbook</h3>
<strong>Author:</strong> Nihanth Cherukuru, Stanislaw 'Stas' Jarosynski, Philip Austin, VAPOR python cookbook contributors
<p class="my-2">The Visualization and Analysis Platform for Ocean, Atmosphere, and Solar Researchers (VAPOR) provides an interactive 3D visualization environment for exploratory visual analysis and the production of captivating animations and high-quality images. VAPOR runs on most UNIX and Windows systems equipped with modern 3D graphics cards. </p>
<p class="my-2"><span class="badge bg-primary mybadges">3D-Visualizations</span>
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Numpy</span>
<span class="badge bg-primary mybadges">Particles</span>
<span class="badge bg-primary mybadges">Vapor</span>
<span class="badge bg-primary mybadges">Weather</span>
<span class="badge bg-primary mybadges">Xarray</span></p>
<p class="mt-3 mb-0"><a href="https://projectpythia.org/vapor-python-cookbook/README.html" class="btn btn-outline-primary btn-block">Visit Website</a></p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">3D-Visualizations</span>
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Numpy</span>
<span class="badge bg-primary mybadges">Particles</span>
<span class="badge bg-primary mybadges">Vapor</span>
<span class="badge bg-primary mybadges">Weather</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/vapor-python-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/vapor-python-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/vapor-python-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/656355302"><img alt="DOI" src="https://zenodo.org/badge/656355302.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card cartopy datashader geocat-viz matplotlib metpy seaborn visualization

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/advanced-viz-cookbook/main/advancedvizcookbook.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/advanced-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Advanced Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Julia Kent, Anissa Zacharias, Orhan Eroglu, Philip Chmielowiec, John Clyne, Advanced Visualization Cookbook contributors</p>
<p class="my-2">This Cookbook demonstrates advanced plotting routines using the Python packages matplotlib, cartopy, metpy, and geocat-viz. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cartopy</span>
<span class="badge bg-primary mybadges">Datashader</span>
<span class="badge bg-primary mybadges">Geocat-Viz</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Metpy</span>
<span class="badge bg-primary mybadges">Seaborn</span>
<span class="badge bg-primary mybadges">Visualization</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/advanced-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/advanced-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/advanced-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/671205314"><img alt="DOI" src="https://zenodo.org/badge/671205314.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card cartopy datashader holoviews hvplot visualization

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/unstructured-grid-viz-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/unstructured-grid-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Unstructured Grids Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Orhan Eroglu, Philip Chmielowiec, Rajeev Jain, Ian Franda, Unstructured Grids Visualization Cookbook contributors</p>
<p class="my-2">This Cookbook is a comprehensive showcase of workflows  </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cartopy</span>
<span class="badge bg-primary mybadges">Datashader</span>
<span class="badge bg-primary mybadges">Holoviews</span>
<span class="badge bg-primary mybadges">Hvplot</span>
<span class="badge bg-primary mybadges">Visualization</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/unstructured-grid-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/669999524"><img alt="DOI" src="https://zenodo.org/badge/669999524.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card atmosphere climate climate-model dask geospatial intake-esm land-model matplotlib sustainability xarray zarr

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/na-cordex-viz-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/na-cordex-viz-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">NA-CORDEX Visualization Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Brian Bonnlander, Seth McGinnis, Anderson Banihirwe, Eric Nienhouse, Jeff de La Beaujardière, NA-CORDEX Visualization Cookbook contributors</p>
<p class="my-2">A notebook for visualizing data from the NA-CORDEX dataset. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Atmosphere</span>
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Climate-Model</span>
<span class="badge bg-primary mybadges">Dask</span>
<span class="badge bg-primary mybadges">Geospatial</span>
<span class="badge bg-primary mybadges">Intake-Esm</span>
<span class="badge bg-primary mybadges">Land-Model</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Sustainability</span>
<span class="badge bg-primary mybadges">Xarray</span>
<span class="badge bg-primary mybadges">Zarr</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/na-cordex-viz-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/na-cordex-viz-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/na-cordex-viz-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/635958518"><img alt="DOI" src="https://zenodo.org/badge/635958518.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2024 climate xeofs

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/eofs-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/eofs-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">EOFs Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Robert R. Ford, EOFs Cookbook contributors</p>
<p class="my-2">Description of empirical orthogonal function (EOF) analysis and examples of its application to climate data. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Xeofs</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/eofs-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/eofs-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/eofs-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/656765685"><img alt="DOI" src="https://zenodo.org/badge/656765685.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2024 cartopy climate-modeling matplotlib oceanography xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/ocean-bgc-cookbook/main/coccolithophore_kristen_krumhardt.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/ocean-bgc-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Ocean Biogeochemistry Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Lev Romashkov, Kristen Krumhardt, Ocean Biogeochemistry Cookbook Contributors</p>
<p class="my-2">This Project Pythia Cookbook covers working with various sources of ocean biogeochemistry data, including Community Earth System Model (CESM) output and observational data. It provides a brief introduction to some metrics important to ocean biogeochemistry, from physical quantities like temperature to<a class="modal-btn"> ... more</a> </p>
</div>
</div>

<div class="modal">
<div class="content">
<img src="https://raw.githubusercontent.com/ProjectPythia/ocean-bgc-cookbook/main/coccolithophore_kristen_krumhardt.png" class="modal-img" />
<h3 class="display-3">Ocean Biogeochemistry Cookbook</h3>
<strong>Author:</strong> Lev Romashkov, Kristen Krumhardt, Ocean Biogeochemistry Cookbook Contributors
<p class="my-2">This Project Pythia Cookbook covers working with various sources of ocean biogeochemistry data, including Community Earth System Model (CESM) output and observational data. It provides a brief introduction to some metrics important to ocean biogeochemistry, from physical quantities like temperature to biological quantities like plankton biomass. It also demonstrates some of the data science techniques used to work with this information, and provides an introduction to the relationship between modeled and observational estimates.</p>
<p class="my-2"><span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Cartopy</span>
<span class="badge bg-primary mybadges">Climate-Modeling</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Oceanography</span>
<span class="badge bg-primary mybadges">Xarray</span></p>
<p class="mt-3 mb-0"><a href="https://projectpythia.org/ocean-bgc-cookbook/README.html" class="btn btn-outline-primary btn-block">Visit Website</a></p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Cartopy</span>
<span class="badge bg-primary mybadges">Climate-Modeling</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Oceanography</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/ocean-bgc-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/ocean-bgc-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/ocean-bgc-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/739552419"><img alt="DOI" src="https://zenodo.org/badge/739552419.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2024 NSF-JetStream2 Paleoclimatology Pyleoclim eofs xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/paleoPCA-cookbook/main/LinkedEarth.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/paleoPCA-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Investigating interhemispheric precipitation changes over the past millennium</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Deborah Khider, Srihari Sundar, Varun Ratnakar</p>
<p class="my-2">This cookbook covers paleoclimate model-data comparison using spatio-temporal pattern obtained using Principal Component Analysis (PCA). </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">NSF-JetStream2</span>
<span class="badge bg-primary mybadges">Paleoclimatology</span>
<span class="badge bg-primary mybadges">Pyleoclim</span>
<span class="badge bg-primary mybadges">Eofs</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/paleoPCA-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/paleoPCA-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/paleoPCA-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/813352705"><img alt="DOI" src="https://zenodo.org/badge/813352705.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Climate Climate-Model Cook-off-2024 Data-Access Intake Intake-esgf Xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/esgf-cookbook/main/notebooks/images/logos/esgf2-us.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/esgf-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">ESGF Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Maxwell A. Grover, Nathan Collier, Carsten Ehbrecht, Jacqueline Nugent, Gerardo A. Rivera Tello</p>
<p class="my-2">A cookbook for working with data from the Earth System Grid Federation. </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Climate</span>
<span class="badge bg-primary mybadges">Climate-Model</span>
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Data-Access</span>
<span class="badge bg-primary mybadges">Intake</span>
<span class="badge bg-primary mybadges">Intake-Esgf</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/esgf-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/esgf-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/esgf-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/721319801"><img alt="DOI" src="https://zenodo.org/badge/721319801.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card Cook-off-2024 data-science fourier-transform geocat-datafiles matplotlib numpy pandas pywavelets scipy signal-analysis wavelet xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/wavelet-cookbook/main/thumbnail.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/wavelet-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Wavelet Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Cora Schneck, Wavelet Cookbook contributors</p>
<p class="my-2">A cookbook to learn to work with wavelets in Python </p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Cook-Off-2024</span>
<span class="badge bg-primary mybadges">Data-Science</span>
<span class="badge bg-primary mybadges">Fourier-Transform</span>
<span class="badge bg-primary mybadges">Geocat-Datafiles</span>
<span class="badge bg-primary mybadges">Matplotlib</span>
<span class="badge bg-primary mybadges">Numpy</span>
<span class="badge bg-primary mybadges">Pandas</span>
<span class="badge bg-primary mybadges">Pywavelets</span>
<span class="badge bg-primary mybadges">Scipy</span>
<span class="badge bg-primary mybadges">Signal-Analysis</span>
<span class="badge bg-primary mybadges">Wavelet</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/wavelet-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/wavelet-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/wavelet-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/815311051"><img alt="DOI" src="https://zenodo.org/badge/815311051.svg" /></a>
</div>
</div>
:::


:::{grid-item-card}
:shadow: md
:class-footer: card-footer
:class-card: tagged-card earth-observation holoviews microwave-remote-sensing odc-stac pystac-client remote-sensing rioxarray sentinel-1 stac xarray

<div class="d-flex gallery-card">
<img src="https://raw.githubusercontent.com/ProjectPythia/eo-datascience-cookbook/main/notebooks/images/logos/tuw-geo_eodc_logo_horizontal.png" class="gallery-thumbnail" />
<div class="container">
<a href="https://projectpythia.org/eo-datascience-cookbook/README.html" class="text-decoration-none"><h4 class="display-4 p-0">Earth Observation Data Science Cookbook</h4></a>
<p class="card-subtitle"><strong>Author:</strong> Wolfgang Wagner, Martin Schobben, Nikolas Pikall, Joseph Wagner, Davide Festa, Felix David Reuß, Luka Jovic, Earth Observation Data Science contributors</p>
<p class="my-2">Earth Observation Data Science Cookbook provides training material centered around Earth Observation data while honoring the Pangeo Philosophy. The examples used in the notebooks represent some of the main research lines of the Remote Sensing Unit at the Department of Geodesy and Geoinformation at the<a class="modal-btn"> ... more</a> </p>
</div>
</div>

<div class="modal">
<div class="content">
<img src="https://raw.githubusercontent.com/ProjectPythia/eo-datascience-cookbook/main/notebooks/images/logos/tuw-geo_eodc_logo_horizontal.png" class="modal-img" />
<h3 class="display-3">Earth Observation Data Science Cookbook</h3>
<strong>Author:</strong> Wolfgang Wagner, Martin Schobben, Nikolas Pikall, Joseph Wagner, Davide Festa, Felix David Reuß, Luka Jovic, Earth Observation Data Science contributors
<p class="my-2">Earth Observation Data Science Cookbook provides training material centered around Earth Observation data while honoring the Pangeo Philosophy. The examples used in the notebooks represent some of the main research lines of the Remote Sensing Unit at the Department of Geodesy and Geoinformation at the TU Wien (Austria). In addition, the content familiarizes the reader with the data available at the EODC (Earth Observation Data Centre For Water Resources Monitoring) as well as the computational resources to process large amounts of data.</p>
<p class="my-2"><span class="badge bg-primary mybadges">Earth-Observation</span>
<span class="badge bg-primary mybadges">Holoviews</span>
<span class="badge bg-primary mybadges">Microwave-Remote-Sensing</span>
<span class="badge bg-primary mybadges">Odc-Stac</span>
<span class="badge bg-primary mybadges">Pystac-Client</span>
<span class="badge bg-primary mybadges">Remote-Sensing</span>
<span class="badge bg-primary mybadges">Rioxarray</span>
<span class="badge bg-primary mybadges">Sentinel-1</span>
<span class="badge bg-primary mybadges">Stac</span>
<span class="badge bg-primary mybadges">Xarray</span></p>
<p class="mt-3 mb-0"><a href="https://projectpythia.org/eo-datascience-cookbook/README.html" class="btn btn-outline-primary btn-block">Visit Website</a></p>
</div>
</div>


+++

<div class="tagsandbadges">
<span class="badge bg-primary mybadges">Earth-Observation</span>
<span class="badge bg-primary mybadges">Holoviews</span>
<span class="badge bg-primary mybadges">Microwave-Remote-Sensing</span>
<span class="badge bg-primary mybadges">Odc-Stac</span>
<span class="badge bg-primary mybadges">Pystac-Client</span>
<span class="badge bg-primary mybadges">Remote-Sensing</span>
<span class="badge bg-primary mybadges">Rioxarray</span>
<span class="badge bg-primary mybadges">Sentinel-1</span>
<span class="badge bg-primary mybadges">Stac</span>
<span class="badge bg-primary mybadges">Xarray</span>
<div>
<a class="reference external" href="https://github.com/ProjectPythia/eo-datascience-cookbook/actions/workflows/nightly-build.yaml"><img alt="nightly-build" src="https://github.com/ProjectPythia/eo-datascience-cookbook/actions/workflows/nightly-build.yaml/badge.svg" /></a>
<a class="reference external" href="https://binder.projectpythia.org/v2/gh/ProjectPythia/eo-datascience-cookbook.git/main"><img alt="Binder" src="https://binder.projectpythia.org/badge_logo.svg" /></a>
<a class="reference external" href="https://zenodo.org/badge/latestdoi/830421828"><img alt="DOI" src="https://zenodo.org/badge/830421828.svg" /></a>
</div>
</div>
:::


<div class="modal-backdrop"></div>
<script src="../html/_static/custom.js"></script>
