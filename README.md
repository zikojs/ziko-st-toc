# ziko-st-toc

[![ziko-st-banner](https://github.com/zikojs/ziko-st-toc/blob/main/assets/banner.png?raw=true)](https://github.com/zikojs)


Zikojs based Interactive Table of Contents component for Streamlit.

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
[![Star](https://img.shields.io/github/stars/zakarialaoui10/ziko.js?style=social)](https://github.com/zakarialaoui10/ziko.js)


## License 
This projet is licensed under the terms of MIT License 
