# Get started
This guide will help you install and use ziko-st-toc, a simple component that generates a Table of Contents (TOC) for your Streamlit apps.

It automatically extracts headings from Markdown content and renders a navigable sidebar TOC.

## Installation

Install the package from PyPI:

```bash
pip install ziko-st-toc
```

## Basic Usage

```python
import streamlit as st

from ziko_st_toc import table_of_contents

st.title('Streamlit Table Of contents')

with st.sidebar:
   table_of_contents()

st.header('Header I')
# Content ..
st.header('Header II')
# Content ..
st.subheader('Sub Header II-1')
# Content ..
st.subheader('Sub Header II-2')
# Content ..
st.subheader('Sub Header II-3')
# Content ..
st.header('Header III')
# Content ..
```