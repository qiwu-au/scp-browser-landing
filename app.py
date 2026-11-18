# app.py — AU-branded landing page of the kidney single-cell proteome browsers

from html import escape
from pathlib import Path

import streamlit as st

# ============================ CONFIGURE HERE ============================ #
APP_TITLE     = "Kidney Single-Cell Proteome Browsers"
CONTACT_NAME  = "Qi Wu"
CONTACT_EMAIL = "qi.wu@biomed.au.dk"
LAST_MODIFIED = "2026-11-19"

# The page shows one panel per study. A panel holds the browsers of that study and, in its top right
# corner, the small icon links that belong to them (Methods, Code).
#
# To add a browser to a study, copy one entry of its "browsers" list and edit it.
# To add a new study with its own Methods and Code, copy the template below the first study.
#
#   title     heading of the panel
#   methods   the methods of this study: a text file in this folder (Markdown, shown as a page of this
#             site) or a web address; "" = no Methods icon
#   code      web address of the analysis code; "" = no Code icon
#   links     optional further icon links: [{"label": "Data", "icon": ":material/database:", "url": "https://..."}]
#             (icon names: https://fonts.google.com/icons)
#   browsers  the cards of the panel, in this order:
#       name    title of the card
#       tags    short labels above the title (species, tissue, condition, ...)
#       blurb   one or two sentences
#       url     address of the deployed browser
#       status  "live" = card with an "Open browser" button; "soon" = greyed card without a button
STUDIES = [
    {
        "title": "Mouse kidney and distal convoluted tubule",
        "methods": "methods.md",
        "code": "https://github.com/qiwu-au/scp_mouse_kidney_dct",
        "browsers": [
            {
                "name": "Mouse Kidney",
                "tags": ["Mouse", "Total kidney"],
                "blurb": "Total mouse kidney: 712 cells and 4,054 proteins, with the cell types reported in the manuscript.",
                "url": "https://scp-browser-kidney.streamlit.app/",
                "status": "live",
            },
            {
                "name": "Mouse DCT",
                "tags": ["Mouse", "Distal convoluted tubule"],
                "blurb": "DCT cells of mice on a control diet (729 cells) and on a zero-potassium diet (702 cells): "
                         "each diet on its own, and a page that compares the two.",
                "url": "https://scp-browser-dct.streamlit.app/",
                "status": "live",
            },
        ],
    },
    # Template for a further study (remove the leading "# " and fill in):
    # {
    #     "title": "Human kidney",
    #     "methods": "methods_human_kidney.md",      # put this file next to app.py, or give a web address
    #     "code": "https://github.com/your-account/your-repository",
    #     "browsers": [
    #         {
    #             "name": "Human Kidney",
    #             "tags": ["Human", "Total kidney"],
    #             "blurb": "One or two sentences about the data.",
    #             "url": "https://your-app.streamlit.app/",
    #             "status": "live",          # or "soon" while the browser is not online
    #         },
    #     ],
    # },
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

      /* Study panel: heading on the left, its icon links on the right, its browser cards below */
      [class*="st-key-study-"] {{ background:#f7f9fc; border-radius:16px; padding:18px 20px 20px 20px; margin-bottom:6px; }}
      .au-study-title {{ font-size:1.15rem; font-weight:700; line-height:1.3; color:#1b2540; }}
      .au-study-sub {{ font-size:0.85rem; color:{AU_TEXT_MUTED}; margin-top:2px; }}

      /* Browser cards: a grid that wraps by itself as browsers are added */
      .au-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:20px; margin-top:6px; }}
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


def is_web(target: str) -> bool:
    return target.lower().startswith(("http://", "https://"))


def methods_path(study: dict) -> str:
    """Address of a study's methods page on this site: the file name without its ending ("methods.md" -> "methods")."""
    return Path(study["methods"]).stem.replace("_", "-").lower()


def study_links(study: dict, with_methods: bool = True) -> None:
    """The small icon links of one study, in one row at the right."""
    with st.container(horizontal=True, horizontal_alignment="right", gap="small"):
        methods = study.get("methods", "")
        if methods and with_methods:
            st.page_link(methods if is_web(methods) else METHODS_PAGES[methods_path(study)],
                         label="Methods", icon=":material/menu_book:")
        if study.get("code"):
            st.page_link(study["code"], label="Code", icon=":material/code:")
        for link in study.get("links", []):
            st.page_link(link["url"], label=link["label"], icon=link.get("icon"))


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


def study_panel(study: dict, number: int) -> None:
    """One study: heading, its icon links, and its browser cards, inside one frame."""
    browsers = study.get("browsers", [])
    with st.container(border=True, key=f"study-{number}"):
        left, right = st.columns([3, 2], vertical_alignment="center")
        with left:
            count = f"{len(browsers)} browser{'s' if len(browsers) != 1 else ''}"
            st.markdown(f"<div class='au-study-title'>{escape(study['title'])}</div>"
                        f"<div class='au-study-sub'>{count}</div>", unsafe_allow_html=True)
        with right:
            study_links(study)
        st.markdown("<div class='au-grid'>" + "".join(card_html(b) for b in browsers) + "</div>",
                    unsafe_allow_html=True)


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
- **Methods** and **Code**: the small links at the top right of each panel below belong to the browsers in that panel.
            """
        )

    st.write("")
    for number, study in enumerate(STUDIES):
        study_panel(study, number)
    footer()


# ---------- pages: methods (one per study that keeps its methods in a text file here) ----------
def methods_page(study: dict):
    def page() -> None:
        header("Methods")
        names = ", ".join(b["name"] for b in study.get("browsers", []))
        st.markdown(f"<div class='au-study-title'>{escape(study['title'])}</div>"
                    f"<div class='au-study-sub'>Browsers: {escape(names)}</div>", unsafe_allow_html=True)
        left, right = st.columns([1, 1], vertical_alignment="center")
        with left:
            st.page_link(HOME_PAGE, label="Back to the browsers", icon=":material/arrow_back:")
        with right:
            study_links(study, with_methods=False)
        text, _ = st.columns([4, 1])
        with text:
            st.markdown((APP_DIR / study["methods"]).read_text(encoding="utf-8"), unsafe_allow_html=True)
        footer()
    return page


HOME_PAGE = st.Page(home, title="Browsers", url_path="browsers", default=True)
METHODS_PAGES = {
    methods_path(study): st.Page(methods_page(study), title=f"Methods: {study['title']}", url_path=methods_path(study))
    for study in STUDIES if study.get("methods") and not is_web(study["methods"])
}
st.navigation([HOME_PAGE, *METHODS_PAGES.values()], position="hidden").run()
