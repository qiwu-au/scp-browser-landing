# app.py — AU-branded landing page of the kidney single-cell proteome browsers

from html import escape
from pathlib import Path

import streamlit as st

# ============================ CONFIGURE HERE ============================ #
APP_TITLE     = "Kidney Single-Cell Proteome Browsers"
CONTACT_NAME  = "Qi Wu"
CONTACT_EMAIL = "qi.wu@biomed.au.dk"
LAST_MODIFIED = "2026-11-18"

# Browsers, shown as cards in this order. To add a browser, copy one entry and edit it.
#   name    title of the card
#   group   section of the page; section headings appear once there are two or more groups
#   tags    short labels above the title (species, tissue, condition, ...)
#   blurb   one or two sentences
#   url     address of the deployed browser
#   status  "live" = card with an "Open browser" button; "soon" = greyed card without a button
BROWSERS = [
    {
        "name": "Mouse Kidney",
        "group": "Mouse",
        "tags": ["Mouse", "Total kidney"],
        "blurb": "Total mouse kidney: 712 cells and 4,054 proteins, with the cell types reported in the manuscript.",
        "url": "https://scp-browser-kidney.streamlit.app/",
        "status": "live",
    },
    {
        "name": "Mouse DCT",
        "group": "Mouse",
        "tags": ["Mouse", "Distal convoluted tubule"],
        "blurb": "DCT cells of mice on a control diet (729 cells) and on a zero-potassium diet (702 cells): "
                 "each diet on its own, and a page that compares the two.",
        "url": "https://scp-browser-dct.streamlit.app/",
        "status": "live",
    },
    # Template for a further browser (remove the leading "# " and fill in):
    # {
    #     "name": "Human Kidney",
    #     "group": "Human",
    #     "tags": ["Human", "Total kidney"],
    #     "blurb": "One or two sentences about the data.",
    #     "url": "https://your-app.streamlit.app/",
    #     "status": "live",          # or "soon" while the browser is not online
    # },
]

# Small icon links next to the title. "page" opens a page of this site ("methods"), "url" another site.
# Icons are Material Symbols names: https://fonts.google.com/icons
RESOURCES = [
    {"label": "Methods", "icon": ":material/menu_book:", "page": "methods"},
    {"label": "Code", "icon": ":material/code:", "url": "https://github.com/qiwu-au/scp_mouse_kidney_dct"},
]
# ======================================================================= #

st.set_page_config(page_title=APP_TITLE, layout="wide")

# ---------- AU brand-ish colors ----------
AU_BLUE       = "#002F6C"  # primary
AU_BLUE_LIGHT = "#E8EEF8"  # light background accent
AU_TEXT_MUTED = "rgba(0,0,0,0.65)"

# ---------- paths / logo ----------
APP_DIR  = Path(__file__).parent
AU_LOGO  = APP_DIR / "assets" / "au_logo.png"
METHODS  = APP_DIR / "methods.md"
LOGO_PX  = 160  # adjust 160–240 if you want

# ---------- styles ----------
st.markdown(
    f"""
    <style>
      .block-container {{ padding-top: 3rem; max-width: 1120px; }}
      h1 {{ margin-top: 0.2rem; }}
      .au-muted {{ color:{AU_TEXT_MUTED}; font-size:0.95rem; }}
      .au-callout {{
        background:{AU_BLUE_LIGHT}; border-left:4px solid {AU_BLUE};
        padding:10px 14px; border-radius:10px; color:rgba(0,0,0,0.85); margin-top:0.35rem;
      }}

      /* Browser cards: a grid that wraps by itself as browsers are added */
      .au-group {{
        font-size:0.8rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;
        color:{AU_TEXT_MUTED}; margin:1.4rem 0 0.6rem;
      }}
      .au-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:20px; }}
      .au-card {{
        display:flex; flex-direction:column;
        border:1px solid rgba(0,0,0,0.10); border-radius:14px; padding:18px; background:#fff;
        transition:box-shadow .15s ease, transform .05s ease;
      }}
      .au-card:hover {{ box-shadow:0 6px 20px rgba(0,0,0,.08); transform:translateY(-2px); }}
      .au-card.soon {{ background:#fafafa; }}
      .au-card.soon:hover {{ box-shadow:none; transform:none; }}
      .au-card.soon .au-card-title, .au-card.soon .au-card-text {{ color:rgba(0,0,0,0.5); }}
      .au-tags {{ display:flex; flex-wrap:wrap; align-items:center; gap:6px; margin-bottom:10px; }}
      .au-tag {{
        font-size:0.75rem; padding:2px 9px; border-radius:999px;
        background:#f1f3f5; color:rgba(0,0,0,0.7);
      }}
      .au-pill {{
        font-size:0.75rem; font-weight:700; padding:2px 10px; border-radius:999px;
        background:{AU_BLUE_LIGHT}; color:{AU_BLUE}; margin-left:auto;
      }}
      .au-pill.soon {{ background:#ececec; color:rgba(0,0,0,0.55); }}
      .au-card-title {{ font-size:1.35rem; font-weight:700; line-height:1.25; color:#1b2540; margin-bottom:6px; }}
      .au-card-text {{ font-size:0.95rem; line-height:1.5; color:rgba(0,0,0,0.8); flex:1; }}
      a.au-btn {{
        align-self:flex-start; margin-top:16px;
        text-decoration:none; padding:8px 14px; border-radius:10px; font-weight:700;
        border:1px solid {AU_BLUE}; color:{AU_BLUE};
      }}
      a.au-btn:hover {{ background:{AU_BLUE}; color:#fff; }}

      /* Small icon links (Methods, Code, back link) */
      [data-testid="stPageLink"] {{ margin:0; }}
      [data-testid="stPageLink-NavLink"] {{
        border:1px solid rgba(0,47,108,0.30); border-radius:999px; padding:3px 12px 3px 9px;
        width:fit-content; background:#fff; gap:5px;
      }}
      [data-testid="stPageLink-NavLink"] p {{ color:{AU_BLUE}; font-weight:600; font-size:0.85rem; }}
      [data-testid="stPageLink-NavLink"] [data-testid="stIconMaterial"] {{ color:{AU_BLUE}; font-size:1.05rem; }}
      [data-testid="stPageLink-NavLink"]:hover {{ background:{AU_BLUE_LIGHT}; }}
    </style>
    """,
    unsafe_allow_html=True,
)


def resource_links(skip: str = "") -> None:
    """The small icon links, in one row (the link to the page that is open is left out)."""
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        for item in RESOURCES:
            if item.get("page") and item["page"] == skip:
                continue
            target = PAGES[item["page"]] if item.get("page") else item["url"]
            st.page_link(target, label=item["label"], icon=item.get("icon"))


def header(title: str, skip: str = "") -> None:
    left, right = st.columns([1, 1], vertical_alignment="center")
    with left:
        if AU_LOGO.exists():
            st.image(str(AU_LOGO), width=LOGO_PX)
    with right:
        resource_links(skip)
    st.title(title)


def footer() -> None:
    st.markdown("---")
    st.markdown(
        f"""
        <div class="au-muted">
          <div>Questions or feedback? Contact <a href="mailto:{CONTACT_EMAIL}">{CONTACT_NAME}</a>.</div>
          <div style="margin-top: 0.25rem;">Last modified: {LAST_MODIFIED}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card_html(browser: dict) -> str:
    live = browser.get("status", "live") == "live" and bool(browser.get("url"))
    tags = "".join(f"<span class='au-tag'>{escape(t)}</span>" for t in browser.get("tags", []))
    pill = "<span class='au-pill'>Live</span>" if live else "<span class='au-pill soon'>Coming soon</span>"
    button = (f"<a class='au-btn' href='{escape(browser['url'], quote=True)}' target='_blank' rel='noopener'>"
              "Open browser →</a>") if live else ""
    return (f"<div class='au-card{'' if live else ' soon'}'>"
            f"<div class='au-tags'>{tags}{pill}</div>"
            f"<div class='au-card-title'>{escape(browser['name'])}</div>"
            f"<div class='au-card-text'>{escape(browser.get('blurb', ''))}</div>"
            f"{button}</div>")


def browser_cards() -> None:
    groups: dict[str, list[dict]] = {}
    for browser in BROWSERS:
        groups.setdefault(browser.get("group", ""), []).append(browser)
    parts = []
    for name, members in groups.items():
        if len(groups) > 1 and name:
            parts.append(f"<div class='au-group'>{escape(name)}</div>")
        parts.append("<div class='au-grid'>" + "".join(card_html(b) for b in members) + "</div>")
    st.markdown("".join(parts), unsafe_allow_html=True)


# ---------- page: browsers ----------
def home() -> None:
    header(APP_TITLE)
    st.markdown(
        """
        <div class="au-callout">
          <div><strong>Interactive browsers for single-cell mass-spectrometry proteomics of kidney cells.</strong></div>
          <div>Explore UMAPs, per-cell QC, all identified proteins, marker dotplots, core/unique proteins by cell type,
          and overlay protein abundance.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("How to use these browsers (quick guide)"):
        st.markdown(
            """
- **Sidebar** (in each browser): choose cell types, search a protein (gene symbol, UniProt accession or description), and set the thresholds for “core” and “unique” proteins and the UMAP size. The DCT browser also has a switch between the control and the zero-potassium diet.
- **Overview**: cells, proteins and cell types, with the evidence for each cluster's cell type.
- **Protein table** and **Protein page**: all identified proteins, and one protein by cell type.
- **Cells & UMAP**: the UMAP colored by cell type, by per-cell QC or by the **abundance of a selected protein**.
- **Dotplot**: marker presets or your own protein list.
- **Core & unique**: proteins commonly detected in a chosen cell type (core) and rare in others (unique).
- **Per-cell QC**: detected proteins per cell and other QC metrics.
- **Control vs zero-K** (DCT browser): the two diets side by side.
- **Downloads** and **About**: tables as CSV, and how the data and values were produced.
            """
        )

    st.markdown("---")
    browser_cards()
    footer()


# ---------- page: methods ----------
def methods() -> None:
    header("Methods", skip="methods")
    st.page_link(PAGES["home"], label="Back to the browsers", icon=":material/arrow_back:")
    text, _ = st.columns([4, 1])
    with text:
        st.markdown(METHODS.read_text(encoding="utf-8"), unsafe_allow_html=True)
    footer()


PAGES = {
    "home": st.Page(home, title="Browsers", url_path="browsers", default=True),
    "methods": st.Page(methods, title="Methods", url_path="methods"),
}
st.navigation(list(PAGES.values()), position="hidden").run()
