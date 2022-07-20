# Makefile for Sphinx documentation
#


# Oneshell means I can run multiple lines in a recipe in the same shell, so I don't have to
# chain commands together with semicolon
.ONESHELL:

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = source/_build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) ./source

# anaconda support
SHELL=/bin/bash
# Note that the extra activate is needed to ensure that the activate floats env to the front of PATH
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate


.PHONY: help clean html github

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       builds standalone HTML files"
	@echo "  cache      builds standalone HTML files from cache whenever possible"
	@echo "  github     builds website ready to be pushed to GitHub"
	@echo "  rebuild    rebuilds the website in-place, without querying data from HydroShare"
	@echo "  clean      cleans all local build files"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(CONDA_ACTIVATE) $(CONDA_DEFAULT_ENV); python make-gallery-pages.py -g ./source/gallery
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

rebuild: 
	$(CONDA_ACTIVATE) $(CONDA_DEFAULT_ENV); $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

cache:
	$(CONDA_ACTIVATE) $(CONDA_DEFAULT_ENV); python make-gallery-pages.py -g ./source/gallery --cache
	@make rebuild

github:
	@make html
	@cp -a $(BUILDDIR)/html/. docs
	@echo
	@echo "The GitHub pages are in ./docs"

