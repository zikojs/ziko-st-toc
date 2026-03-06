import streamlit as st
from ziko_st_toc import table_of_contents

st.title('Streamlit Table Of contents')

with st.sidebar:
    toc = table_of_contents(style = {
        'borderRadius' : '25px',
        'border' : '3px dotted blue',
        'backgroundColor' : 'none'
    })

st.text(toc)

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
""")
st.subheader('Author')


# st.subheader("Author")
# st.markdown("""
# **Zakaria El Alaoui**

# Developer of the **Zikojs** ecosystem.  
# Focused on building lightweight developer tools and reusable UI components.
# """)

# st.subheader("Dependencies")
# st.markdown("""
# `ziko-st-toc` is designed to be lightweight and has minimal dependencies:

# - **Streamlit** – used to render the component inside Streamlit apps.
# - **JavaScript Table of Contents logic** bundled in the component frontend.

# The package ships its frontend assets inside the wheel, so no additional setup is required.
# """)
# st.header('About')
# st.subheader('Author')

# st.subheader('Dependencies')

# st.write("""
# **ziko-st-toc** is part of the Ziko ecosystem.

# Author: Zakaria El Alaoui  
# GitHub: https://github.com/zikojs/ziko-st-toc

# If you find this project useful, consider supporting it ☕
# """)


