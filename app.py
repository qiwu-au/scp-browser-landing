# app.py — AU-branded landing page for your three browsers

import streamlit as st
from datetime import date
from pathlib import Path

# --------------------------- CONFIGURE HERE --------------------------- #
APP_TITLE     = "Kidney Single-Cell Proteome Browsers"
CONTACT_NAME  = "Qi Wu"
CONTACT_EMAIL = "qi.wu@biomed.au.dk"

# Deployed links (replace with your real URLs or localhost while testing)
BROWSER_LINKS = {
    "Mouse Kidney": {
        "url": "https://scp-browser-kidney.streamlit.app/",
        "blurb": "Mouse kidney single-cell proteome browser",
    },
    "Mouse Kidney (Re-annotated)": {
        "url": "https://scp-browser-kidney-reannotated.streamlit.app/",
        "blurb": "Re-annotated mouse kidney single-cell proteome browser (to resolve more cell types)",
    },
    "Mouse DCT": {
        "url": "https://scp-browser-dct.streamlit.app/",
        "blurb": "Mouse distal convoluted tubule (DCT) single-cell proteome browser",
    },
}
# --------------------------------------------------------------------- #

st.set_page_config(page_title=APP_TITLE, layout="wide")

st.markdown(
    """
    <style>
      /* Give the logo room so it doesn't get clipped */
      .block-container { padding-top: 1.5rem; }

      /* Tighten H1 spacing */
      h1 { margin-top: 0.2rem; }

      /* Trim any extra top padding in the first column (logo/title area) */
      [data-testid="stVerticalBlock"] > div:first-child { padding-top: 0rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- AU brand-ish colors ----------
AU_BLUE       = "#002F6C"  # primary
AU_BLUE_LIGHT = "#E8EEF8"  # light background accent
AU_TEXT_MUTED = "rgba(0,0,0,0.65)"

# ---------- paths / logo ----------
APP_DIR   = Path(__file__).parent
ASSETS    = APP_DIR / "assets"
AU_LOGO   = ASSETS / "au_logo.png"
has_logo  = AU_LOGO.exists()

# ---------- styles ----------
st.markdown(
    f"""
    <style>
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
      .au-header-right {{ text-align:right; }}
      .au-header-title {{ margin-bottom:4px; }}
      /* NEW: subtle AU-blue callout for the intro text */
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

# ---------- header (flat, left-aligned) ----------
LOGO_PX = 160  # adjust 160–240 if you want

if has_logo:
    st.image(str(AU_LOGO), width=LOGO_PX)

st.title(APP_TITLE)

# AU-blue highlighted intro (left-aligned, full width of the page container)
st.markdown(
    """
    <div class="au-callout">
      <div><strong>Interactive browsers for single-cell mass-spectrometry proteomics of kidney cells.</strong></div>
      <div>Explore UMAPs, per-cell QC, all identified proteins, core/unique proteins by cell type, and overlay protein abundance.</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- quick instructions ----------
with st.expander("How to use these browsers (quick guide)"):
    st.markdown(
        """
- **Filters** (left sidebar in each browser): choose datasets and cell types; adjust thresholds for “core” and “unique” proteins.
- **UMAPs**:
  - The main UMAP shows cell embedding by cell type.
  - The overlay UMAP colors cells by **abundance of a selected protein** (search by UniProt, gene symbol, or description).
  - A single **UMAP size** slider resizes both UMAPs.
- **Protein summary table**: lists all proteins identified or a selected protein (search by UniProt, gene symbol, or description).
- **Core/Unique proteins**: list proteins commonly detected in a chosen cell type (core) and rare in others (unique). Export tables as CSV.
- **Per-cell QC**: inspect detected proteins per cell and summary QC metrics.
        """
    )

st.markdown("---")

# ---------- three browser cards ----------
def browser_card(name: str, url: str, blurb: str):
    st.markdown(f"### {name} <span class='au-pill'>Live</span>", unsafe_allow_html=True)
    st.markdown(f"<div class='au-card'>{blurb}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='au-linkbtn'><a href='{url}' target='_blank'>Open {name} →</a></div>",
        unsafe_allow_html=True,
    )

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    browser_card("Mouse Kidney", BROWSER_LINKS["Mouse Kidney"]["url"], BROWSER_LINKS["Mouse Kidney"]["blurb"])
with c2:
    browser_card("Mouse Kidney (Re-annotated)", BROWSER_LINKS["Mouse Kidney (Re-annotated)"]["url"], BROWSER_LINKS["Mouse Kidney (Re-annotated)"]["blurb"])
with c3:
    browser_card("Mouse DCT", BROWSER_LINKS["Mouse DCT"]["url"], BROWSER_LINKS["Mouse DCT"]["blurb"])

st.markdown("---")

# ---------- footer ----------
st.markdown(
    f"""
    <div class="au-muted">
      <div>Questions or feedback? Contact <a href="mailto:{CONTACT_EMAIL}">{CONTACT_NAME}</a>.</div>
      <div style="margin-top: 0.25rem;">Last modified: {date.today().isoformat()}</div>
    </div>
    """,
    unsafe_allow_html=True,
)