# ziko-st-toc


[![PyPI version](https://img.shields.io/pypi/v/ziko-st-toc.svg)](https://pypi.org/project/ziko-st-toc/)
[![Downloads](https://img.shields.io/pypi/dm/ziko-st-toc)](https://pypi.org/project/ziko-st-toc/)
[![License](https://img.shields.io/pypi/l/ziko-st-toc.svg)](https://github.com/zikojs/ziko-st-toc/blob/main/LICENSE)
[![Netlify Status](https://api.netlify.com/api/v1/badges/04130c58-4a37-4437-8833-bd019eeb5983/deploy-status)](https://app.netlify.com/projects/ziko-st-toc/deploys)


[![ziko-st-banner](https://github.com/zikojs/ziko-st-toc/blob/main/assets/banner.png?raw=true)](https://github.com/zikojs)


A Streamlit component that generates an interactive Table of Contents (TOC) with smooth scrolling and navigation.

## Showcase

![ziko-st-toc demo](https://raw.githubusercontent.com/zikojs/ziko-st-toc/refs/heads/main/assets/demo.gif)

Visit : https://ziko-st-toc.streamlit.app/

## Installation instructions

```sh
pip install ziko-st-toc
```

## Usage instructions

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

## ⭐️ Show your support <a name="support"></a>

If you appreciate the library, kindly demonstrate your support by giving it a star!<br>
<!-- [![Star](https://img.shields.io/github/stars/zikojs/ziko-st-toc?style=social)](https://github.com/zikojs/ziko-st-toc) -->


## License 
This projet is licensed under the terms of MIT License 
