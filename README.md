# ziko-st-toc

[![ziko-st-banner](https://raw.githubusercontent.com/zakarialaoui10/ziko-i18n/606f5caf87b1d41184c7989c11e5272c68a375ab/assets/banner.svg)](https://github.com/zakarialaoui10/zikojs)


Zikojs based Interactive Table of Contents component for Streamlit.

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

## Licence