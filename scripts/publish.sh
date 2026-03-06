#!/usr/bin/env bash
set -e  # exit immediately if a command fails
pip install --upgrade twine
twine upload dist/*