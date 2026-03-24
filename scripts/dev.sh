#!/usr/bin/env bash

# Start frontend
(cd ziko_st_toc/frontend && npm i && npm run dev) &

# Start streamlit
streamlit run example.py

# Kill frontend when streamlit exits
kill $(jobs -p)