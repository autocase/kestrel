#!/bin/sh
cd docs
# Generate Sphinx source files
sphinx-apidoc -f -o source ../app
# Make static files
make html
cd ..
