---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "ziko-st-toc"
  text: "Streamlit Table of Contents generator"
  tagline: Automatically generate a Table of Contents for your Streamlit apps.
  actions:
    - theme: brand
      text: Demo
      link: https://ziko-st-toc-demo.streamlit.app/
    - theme: alt
      text: View on GitHub
      link: https://github.com/zikojs/ziko-st-toc
    # - theme: alt
    #   text: API Examples
    #   link: /api-examples

features:
  - title: 📑 Automatic Table of Contents
    details: generates a Table of Contents from st.title, st.header, st.subheader, and headings from st.markdown and st.html.
  - title: 🧭 Clickable Navigation
    details: Each entry in the TOC links directly to the corresponding section in the page for quick navigation.
  - title: 🪜 Hierarchical Structure
    details: Headings are organized into a nested structure, preserving the hierarchy of h1...h6
  - title: 🎯 Depth Control
    details : Limit how deep the table of contents goes.
  - title : 🔁 Reactive
    details : Works naturally with Streamlit's rerun system and reacts to dynamic content, user inputs ...
---

