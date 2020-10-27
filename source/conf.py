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
    'sphinxcontrib.exceltable',
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



nbsphinx_thumbnails = {
    'gallery/thumbnail-from-conf-py': 'gallery/a-local-file.png',
   
}

tagtoctree_tag = 'tagtoctree'

# Sphinx Gallery

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

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

