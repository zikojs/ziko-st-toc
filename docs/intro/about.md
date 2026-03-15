# About 
## What is ziko-st-toc?

ziko-st-toc is a Streamlit plugin that automatically generates a Table of Contents (TOC) for your app.

It helps organize long pages by detecting headings and building a structured, clickable TOC, without requiring manual setup.

It supports headings from multiple sources:

- `st.title()`
- `st.header()`
- `st.subheader()`
- Markdown content via `st.markdown()`
<!-- - HTML headings via st.markdown(..., unsafe_allow_html=True) -->

This ensures the TOC always reflects the structure of your Streamlit page.

## How It Works ?

- **Backend (Python / Streamlit)**: Handles detection of headings and renders the TOC container.
- **Frontend (zikojs)**: Powers the interactive UI, smooth scrolling, and hierarchical display of the TOC.

By combining Python and [zikojs](https://github.com/zikojs/ziko), ziko-st-toc offers a lightweight, reactive, and modern TOC experience for Streamlit apps.

## Why Use ziko-st-toc ?

Navigating long documentation-style apps, tutorials, or dashboards in Streamlit can be cumbersome.
ziko-st-toc solves this by:

- Detecting headings automatically from multiple sources
- Building a hierarchical TOC
- Allowing users to jump quickly to sections
- Reacting dynamically when the app reruns