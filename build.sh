#!/bin/bash

python make-gallery-pages.py -g ./source/gallery && \
sphinx-build -b html source _build
