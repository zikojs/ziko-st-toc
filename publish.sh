#!/usr/bin/env bash
set -e  # exit immediately if a command fails
rm -rf dist/*
uv build
pip install --upgrade twine
twine upload dist/*

