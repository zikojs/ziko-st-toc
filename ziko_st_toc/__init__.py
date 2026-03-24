import streamlit as st

out = st.components.v2.component(
    "ziko-st-toc.ziko_st_toc",
    js="index-*.js",
    css=""" 
    .zextra-toc {
        position: sticky;
        top: 20px;
        max-width: 250px;
        padding: 10px;
        background: var(--st-background-color);
        border: 1px solid var(--st-border-color);
        font-family: var(--st-font);
    }

    .zextra-toc ul {
        list-style: none;
        padding-left: 0;
    }

    .zextra-toc li {
        margin-bottom: 5px;
    }

    .zextra-toc a {
        text-decoration: none;
        color: #007bff;
        color : var(--st-link-color);

    }

    .zextra-toc a:hover {
        text-decoration: underline;
        color : var(--st-link-underline);
    }
    """,
    html="""
    <div data-engine="zikojs"></div>
    """,
)

def table_of_contents(
        style = None,
        useHash = False,
        level = 2,
        name = "", 
        key = None
    ):
    """
    Render a Table of Contents for the current Streamlit page.

    The component scans the page for headings (`h1`–`h6`) and generates
    a navigation list that allows users to quickly jump to sections.

    Parameters
    ----------
    level : int, default=2
        Maximum heading level to include in the table of contents.
        For example:
        - 1 → only `h1`
        - 2 → `h1`, `h2`
        - 3 → `h1`, `h2`, `h3`
        - up to `h6`.

    style : dict, optional
        Custom CSS styles applied to the table of contents container.
        Example:
        `{"position": "sticky", "top": "1rem"}`

    usehash : bool, default=True
        If True, clicking a TOC link updates the page URL hash (`#section-id`)
        to reflect the selected heading.

    key : str or None, optional
        Unique key for the component instance. Needed when using multiple
        TOC components in the same app.

    Returns
    -------
    dict or None
        Returns a dictionary containing interaction data from the component.
        Example:
        `{"last_clicked_id": "usage"}`
    """

    component_value = out(
        name = name,
        key = key,
        style = style,
        useHash = useHash,
        level = level
    )

    return component_value