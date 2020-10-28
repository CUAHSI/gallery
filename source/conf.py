# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sys
from sphinx_gallery.sorting import FileNameSortKey


# -- Project information -----------------------------------------------------

project = 'BuildDocs'
copyright = '2020'
author = 'Gaby Garcia'

# The full version, including alpha/beta/rc tags
version = '3.7.2'
release = 'version'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode', 
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.matlab',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'numpydoc',
    'sphinxcontrib.images',
    'sphinx_git',
    'nbsphinx',
    'sphinx_gallery.load_style',
    'sphinx.ext.mathjax',
    'sphinx_gallery.load_style',
    'sphinx_copybutton',
    'sphinxcontrib.bibtex',
    'sphinx_gallery.gen_gallery',
]



# Generate Autosummary even if no references
autosummary_generate = 'True'

tagtoctree_tag = 'tagtoctree'

# Sphinx Gallery


sphinx_gallery_conf = {
    
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',# path to where to save gallery generated output
     'plot_gallery': 'True',
     'download_all_examples': 'True',
     'first_notebook_cell': ("# This cell is added by sphinx-gallery\n"
                            "# It can be customized to whatever you like\n"
                            "%matplotlib inline"),


'binder': {
     # Required keys
     'org': 'CUAHSI',
     'repo': 'gallery',
     'branch': 'master',  # Can be any branch, tag, or commit hash. Use a branch that hosts your docs.
     'binderhub_url': 'https://mybinder.org',  # Any URL of a binderhub deployment. Must be full URL (e.g. https://mybinder.org).
     'dependencies': './binder/requirements.txt',
     # Optional keys
    # 'filepath_prefix': '<prefix>' # A prefix to prepend to any filepaths in Binder links.
     'notebooks_dir': 'notebooks', # Jupyter notebooks for Binder will be copied to this directory (relative to built documentation root).
    # 'use_jupyter_lab': <bool> # Whether Binder links should start Jupyter Lab instead of the Jupyter Notebook interface.
     },


     
}

plot_gallery= 'True'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'


html_theme_options = {
    'github_button': 'false',
    'github_user': 'gdg12',
    'github_repo': 'alabaster',
    'github_type': 'fork',
}


html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "gdg12",  # Username
    "github_repo": "FinalDataAnalyticsProject",  # Repo name
    "github_version": "master",  # Version
    "last_updated": True,
    "conf_py_path": "/Gallery/source/conf.py",  # Path in the checkout to the docs root
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


