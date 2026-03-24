import streamlit as st
from ziko_st_toc import table_of_contents

st.title('Streamlit Table Of contents')

with st.sidebar:
    toc = table_of_contents(
        # style = {
        # 'borderRadius' : '5px',
        # },
        # useHash = False
    )

# st.text(toc)

st.header('Overview')
st.write("""
`ziko-st-toc` is a lightweight **Table of Contents component for Streamlit**.

It automatically scans the page for headings (`st.title`, `st.header`, `st.subheader`, etc.)
and generates a clickable navigation menu.
""")

st.header('Features')
st.write("""
- 📑 Auto-detects headers
- 📌 Click to jump to sections
- 📚 Works with Streamlit layouts (columns, sidebar)
- ⚡ Lightweight custom component
""")


## Usage
st.header('Usage')
st.subheader('Install')
st.code('pip install ziko-st-toc', language="bash")

st.subheader('Basic example')
st.code(
"""
import streamlit as st
from ziko_st_toc import table_of_contents

st.title("My App")

with st.sidebar:
    table_of_contents()

st.header("Overview")
st.write("Content...")

st.header("Usage")
st.write("More content...")
""",
language="python"
)

## 

st.header("About")
st.subheader('Ecosystem')
st.write("""
**ziko-st-toc** is part of the [Zikojs](https://github.com/zikojs) ecosystem.
    """)
st.subheader('Dependencies')
st.markdown("""
|Library|Description
|-|-|
|[ziko](https://github.com/zikojs/ziko)|The core of zikojs ecosystem|
|[zextra](https://github.com/zikojs/zextra)|Extra components for zikojs|
|[streamlit-component-lib](https://github.com/streamlit/streamlit/tree/develop/component-lib)|An npm package that provides support code for creating Streamlit Components.|
|[vite](https://vite.dev/)|Next generation frontend tooling|
""")
st.subheader('Author')
st.write("""
- Github : https://github.com/zakarialaoui10
- Linkedin : https://www.linkedin.com/in/zakaria-elalaoui-810ab41b8/
""")
st.subheader('Support')
st.markdown("""
If you find **ziko-st-toc** useful, you can support the project by:

- ⭐ **Star the repository** on GitHub  
- ⭐ **Star the ZikoJS ecosystem** projects  
- **Sponsor the development** via [Ko-fi](https://ko-fi.com/zakariaelalaoui)
- ...
""")