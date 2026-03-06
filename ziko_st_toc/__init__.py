import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("table_of_contents"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "table_of_contents",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("table_of_contents", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def table_of_contents(level=2, style=None, usehash=True, key=None):
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

    component_value = _component_func(
        level=level,
        style=style or {},
        usehash=usehash,
        key=key,
        default=None,
    )

    return component_value