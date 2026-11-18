# Kidney Single-Cell Proteome Browsers: landing page

The landing page of the kidney single-cell proteome browsers: https://scp-browser-landing.streamlit.app/

The page shows one panel per study. A panel holds the browsers of that study as cards and, in its top right corner, the small icon links that belong to them (Methods, Code).

## Files

| file | content |
| --- | --- |
| `app.py` | the page; everything that is shown comes from the block "CONFIGURE HERE" at its top |
| `methods.md` | the methods of the mouse kidney and DCT study, shown at `/methods` |
| `assets/au_logo.png` | logo |
| `.streamlit/config.toml` | light theme |
| `requirements.txt` | pinned Streamlit version |

## Add a browser to a study

In `app.py`, copy one entry of the study's `browsers` list and edit it:

```python
{
    "name": "Mouse Kidney",
    "tags": ["Mouse", "Total kidney"],
    "blurb": "One or two sentences about the data.",
    "url": "https://your-app.streamlit.app/",
    "status": "live",   # "soon" gives a greyed card without a button
},
```

The new browser shares the Methods and Code links of its study.

## Add a study with its own Methods and Code

1. Write the methods as a Markdown file next to `app.py`, for example `methods_human_kidney.md`. It is shown as a page of this site at `/methods-human-kidney`. A web address can be given instead of a file.
2. In `app.py`, copy the template below the first study in the `STUDIES` list and fill in `title`, `methods`, `code` and the `browsers`.

Leave `methods` or `code` empty (`""`) to show no icon. Further icon links (for example to the data) go into the optional `links` list of a study.

## Run locally

```
pip install -r requirements.txt
streamlit run app.py
```
