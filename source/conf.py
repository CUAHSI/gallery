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

# import m2r to include markdown documents in rst
from m2r import MdInclude

# -- Project information -----------------------------------------------------

project = 'CUAHSI Gallery'
copyright = '2020'
author = 'Anthony Castronova, et al.'

# The full version, including alpha/beta/rc tags
version = '0.1'
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
              'sphinx.ext.napoleon',
              'sphinx.ext.graphviz',
              'sphinx.ext.intersphinx',
#              'sphinxcontrib.matlab',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'numpydoc',
              'sphinxcontrib.images',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx_copybutton',
              'sphinx_panels',
              'recommonmark', # markdown support
              'sphinxcontrib.contentui',
              'sphinx_tabs.tabs',
              'sphinxcontrib.youtube',
]

## sphinx-tabs configuration
sphinx_tabs_disable_tab_closing = True

# Generate Autosummary even if no references
autosummary_generate = True

tagtoctree_tag = 'tagtoctree'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

#source encoding
source_encoding= 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# removing default footer elements
html_show_copyright = False
html_show_sphinx = False
html_last_updated_fmt = None


html_theme_options = {
    
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,

    # suppress MkDocs from appearing above logo
    'logo_only': True,

    # suppress version from being displayed below logo
    'display_version': False,
    
    # suppress 'next' and 'previous' page buttons
    'prev_next_buttons_location': None,

}

html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'relations.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}

html_context = {
   
    "conf_py_path": "/Gallery/source/conf.py",  # Path in the checkout to the docs root
#    'css_files': ['_static/custom.css', '_static/css/theme.css'],
}

html_logo = '_static/cuahsi-logo.png'



# Output file base name for HTML help builder
htmlhelp_basename= 'testdoc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_js_files = ['js/custom.js']

# this is text that will be appended to ..title directives
html_title = 'CUAHSI Gallery'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# This is default language for syntax highlighting in reST and Markdown cells
highlight_language= 'python3' 


# Nbsphinx Configuration

## Use this kernel instead of the one stored in the notebook metadata
nbsphinx_kernel_name = 'python3' 

# suppress_warnings=['nbsphinx',]

nbsphinx_allow_errors = True

## Execute notebooks before conversion: 'always', 'never', 'auto' (default)
nbsphinx_execute= 'never'

## Default Pygments lexer for syntax highlighting in code cells
nbsphinx_codecell_lexer = 'ipython3'

def setup(app):
    # from m2r to make `mdinclude` work
    app.add_config_value('no_underscore_emphasis', False, 'env')
    app.add_config_value('m2r_parse_relative_links', False, 'env')
    app.add_config_value('m2r_anonymous_references', False, 'env')
    app.add_config_value('m2r_disable_inline_math', False, 'env')
    app.add_directive('mdinclude', MdInclude)


# bibtex_bibfiles = ['refs.bib']
