#!/bin/sh
# Install Dev Dependencies
pipenv lock --dev --requirements > dev-requirements.txt
pip install -r dev-requirements.txt
cd docs
# Generate Sphinx source files
sphinx-apidoc -f -o docs/source ../app
# Make static files
make html
cd ..
