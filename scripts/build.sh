#!/usr/bin/env bash
rm -rf dist/*
(cd ziko_st_toc/frontend && npm run build) && uv build