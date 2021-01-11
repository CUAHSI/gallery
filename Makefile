# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = source/_build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) ./source

.PHONY: help clean html github

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       builds standalone HTML files"
	@echo "  github     builds website ready to be pushed to GitHub"
	@echo "  clean      cleans all local build files"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	python make-gallery-pages.py -g ./source/gallery
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

rebuild: 
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

github:
	@make html
	@cp -a $(BUILDDIR)/html/. docs
	@echo
	@echo "The GitHub pages are in ./docs"

