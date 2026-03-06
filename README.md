# ziko-st-toc

Zikojs based Interactive Table of Contents component for Streamlit.

## Installation instructions

```sh
pip install ziko-st-toc
```

## Usage instructions

```python
import streamlit as st

from ziko_st_toc import table_of_contents

value = table_of_contents()

st.write(value)
```

## Local development

1. Start Streamlit from the project root:

   ```sh
   streamlit run ziko_st_toc/example.py
   ```

2. In another terminal, run the Vite dev server from `ziko_st_toc/frontend`:

   ```sh
   npm install
   npm run start
   ```

### Important dev server notes

- The browser connects to the Vite dev server directly. Streamlit does **not** proxy this port, so the Vite port must be reachable from the client just like the Streamlit port.
- Vite listens on the value of `VITE_PORT` (default `3001`). This variable lives in `ziko_st_toc/frontend/.env`. Update that file whenever you need to change the port, and remember that Windows/WSL/Hyper-V or dev containers may silently remap addresses like `3001`.
- If a port is unavailable or blocked by a firewall/mobile connection, set `VITE_PORT=5173` (Vite's default) or any other open port inside the `.env` file before running `npm run start`, and ensure that port is reachable from your browser.
