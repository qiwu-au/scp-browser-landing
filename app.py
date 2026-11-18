# app.py — AU-branded landing page of the kidney single-cell proteome browsers

from pathlib import Path

import streamlit as st

# --------------------------- CONFIGURE HERE --------------------------- #
APP_TITLE     = "Kidney Single-Cell Proteome Browsers"
CONTACT_NAME  = "Qi Wu"
CONTACT_EMAIL = "qi.wu@biomed.au.dk"
LAST_MODIFIED = "2026-11-18"

# Deployed links
BROWSER_LINKS = {
    "Mouse Kidney": {
        "url": "https://scp-browser-kidney.streamlit.app/",
        "blurb": "Total mouse kidney: 712 cells and 4,054 proteins, with the cell types reported in the manuscript.",
    },
    "Mouse DCT": {
        "url": "https://scp-browser-dct.streamlit.app/",
        "blurb": "Distal convoluted tubule (DCT) cells of mice on a control diet (729 cells) and on a zero-potassium "
                 "diet (702 cells): each diet on its own, and a page that compares the two.",
    },
}
METHODS_BLURB = ("Mice and diets, cell sorting, sample preparation, LC-MS, data processing, "
                 "cell-type annotation and the comparison of the two diets.")

# Link to the analysis scripts. The code card appears on the page once a URL is set here.
CODE_URL   = ""
CODE_BLURB = "Python scripts of the analyses."
# --------------------------------------------------------------------- #

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
      /* Give the logo room so it doesn't get clipped */
      .block-container {{ padding-top: 3.5rem; }}
      h1 {{ margin-top: 0.2rem; }}
      .au-muted {{ color:{AU_TEXT_MUTED}; font-size:0.95rem; }}
      .au-pill {{
        display:inline-block; padding:2px 10px; border-radius:999px;
        background:{AU_BLUE_LIGHT}; color:{AU_BLUE}; font-weight:700; font-size:0.8rem;
        margin-left:8px;
      }}
      .au-card {{
        border:1px solid rgba(0,0,0,0.08);
        border-radius:14px; padding:18px 18px 12px 18px; background:#fff;
        transition:box-shadow .15s ease, transform .05s ease;
      }}
      .au-card:hover {{ box-shadow:0 6px 20px rgba(0,0,0,.08); transform:translateY(-2px); }}
      .au-linkbtn a {{
        text-decoration:none; padding:10px 14px; border-radius:10px; font-weight:700;
        border:1px solid {AU_BLUE}; color:{AU_BLUE};
        display:inline-block; margin-top:10px;
      }}
      .au-linkbtn a:hover {{ background:{AU_BLUE}; color:white; }}
      /* Links between the pages of this site: same look as the browser links */
      [data-testid="stPageLink"] {{ margin-top:10px; }}
      [data-testid="stPageLink-NavLink"] {{
        border:1px solid {AU_BLUE}; border-radius:10px; padding:10px 14px;
        width:fit-content; background:transparent;
      }}
      [data-testid="stPageLink-NavLink"] p {{ color:{AU_BLUE}; font-weight:700; font-size:1rem; }}
      [data-testid="stPageLink-NavLink"]:hover {{ background:{AU_BLUE}; }}
      [data-testid="stPageLink-NavLink"]:hover p {{ color:white; }}
      .au-callout {{
        background: {AU_BLUE_LIGHT};
        border-left: 4px solid {AU_BLUE};
        padding: 10px 14px;
        border-radius: 10px;
        color: rgba(0,0,0,0.85);
        margin-top: 0.35rem;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)


def header(title: str) -> None:
    if AU_LOGO.exists():
        st.image(str(AU_LOGO), width=LOGO_PX)
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


def link_card(name: str, url: str, blurb: str, pill: str = "") -> None:
    badge = f" <span class='au-pill'>{pill}</span>" if pill else ""
    st.markdown(f"### {name}{badge}", unsafe_allow_html=True)
    st.markdown(f"<div class='au-card'>{blurb}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='au-linkbtn'><a href='{url}' target='_blank'>Open {name} →</a></div>",
        unsafe_allow_html=True,
    )


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

    cards = [lambda name=name, v=v: link_card(name, v["url"], v["blurb"], "Live") for name, v in BROWSER_LINKS.items()]
    cards.append(methods_card)
    if CODE_URL:
        cards.append(lambda: link_card("Code", CODE_URL, CODE_BLURB))
    for column, card in zip(st.columns(len(cards), gap="large"), cards):
        with column:
            card()

    footer()


def methods_card() -> None:
    st.markdown("### Methods")
    st.markdown(f"<div class='au-card'>{METHODS_BLURB}</div>", unsafe_allow_html=True)
    st.page_link(METHODS_PAGE, label="Open Methods →")


# ---------- page: methods ----------
def methods() -> None:
    header("Methods")
    st.page_link(HOME_PAGE, label="← Back to the browsers")
    text, _ = st.columns([3, 1])
    with text:
        st.markdown(METHODS.read_text(encoding="utf-8"), unsafe_allow_html=True)
    footer()


HOME_PAGE    = st.Page(home, title="Browsers", url_path="browsers", default=True)
METHODS_PAGE = st.Page(methods, title="Methods", url_path="methods")
st.navigation([HOME_PAGE, METHODS_PAGE], position="top").run()
