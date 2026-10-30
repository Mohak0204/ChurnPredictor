"""Shared visual building blocks: page headers, metric cards, status chips, CSS.

Presentation only — no analytical computation. All pages compose these
helpers so styling stays consistent across the app.

Design system: premium black/white canvas, blue accents, Inter typography,
matte card surfaces (flat colour + diffuse soft shadow, no gloss or gradient).
"""

from __future__ import annotations

import streamlit as st

from src import config

# Scoped, maintainable CSS. Selectors use Streamlit's stable data-testid hooks
# plus the custom .cc-* class names this module owns.
_APP_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {{
    --cc-ink: {config.COLOR_INK};
    --cc-text: {config.COLOR_TEXT};
    --cc-muted: {config.COLOR_TEXT_MUTED};
    --cc-hint: {config.COLOR_HINT};
    --cc-border: {config.COLOR_BORDER};
    --cc-border-strong: {config.COLOR_BORDER_STRONG};
    --cc-bg-soft: {config.COLOR_BG_SOFT};
    --cc-blue: {config.COLOR_ACCENT_BLUE};
    --cc-blue-deep: {config.COLOR_ACCENT_BLUE_DEEP};
    --cc-blue-tint: {config.COLOR_ACCENT_BLUE_TINT};
    --cc-shadow-matte: 0 1px 2px rgba(11,18,32,.05), 0 14px 34px -20px rgba(11,18,32,.28);
}}

/* ---------- Canvas and typography ---------- */
html, body, .stApp, [class*="css"] {{
    font-family: {config.FONT_FAMILY};
    background: #FFFFFF;
    color: var(--cc-text);
    font-feature-settings: 'cv02','cv03','cv04';
}}
.block-container {{ padding-top: 2.1rem; padding-bottom: 3.5rem; max-width: 1280px; }}

h1 {{ color: var(--cc-ink); letter-spacing: -0.025em; font-weight: 800; }}
h2 {{ color: var(--cc-ink); letter-spacing: -0.02em; font-weight: 800; font-size: 1.62rem; }}
h3 {{ color: var(--cc-ink); letter-spacing: -0.015em; font-weight: 700; font-size: 1.12rem; }}
h4 {{
    color: var(--cc-ink); font-weight: 700; font-size: 1.0rem; letter-spacing: -0.01em;
    display: flex; align-items: center; margin-top: 1.35rem;
}}
h4::before {{
    content: ""; display: inline-block; width: 3px; height: 15px;
    background: var(--cc-blue); border-radius: 2px; margin-right: 9px;
}}
p, li {{ color: var(--cc-text); line-height: 1.55; }}
strong {{ color: var(--cc-ink); }}
code {{ color: var(--cc-blue-deep); background: var(--cc-blue-tint);
        border: 1px solid #DCE6FA; border-radius: 5px; padding: 0 5px; font-size: .86em; }}
hr {{ border-color: var(--cc-border); }}

/* Muted helper copy */
.cc-note {{ color: var(--cc-muted); font-size: .88rem; }}
[data-testid="stCaptionContainer"], .stCaption, p.caption {{
    color: var(--cc-muted) !important; font-size: .82rem !important;
}}

/* ---------- Metric cards (matte) ---------- */
.cc-metric-card {{
    background: #FFFFFF;
    border: 1px solid var(--cc-border);
    border-radius: 14px;
    padding: 1.05rem 1.2rem;
    box-shadow: var(--cc-shadow-matte);
    transition: border-color .16s ease;
}}
.cc-metric-card:hover {{ border-color: var(--cc-border-strong); }}
.cc-metric-card .cc-metric-label {{
    font-size: .68rem; font-weight: 600; text-transform: uppercase;
    letter-spacing: .1em; color: var(--cc-muted);
}}
.cc-metric-card .cc-metric-value {{
    font-size: 1.72rem; font-weight: 800; letter-spacing: -0.025em;
    color: var(--cc-ink); line-height: 1.15; margin-top: .32rem;
    font-variant-numeric: tabular-nums;
}}
.cc-metric-card .cc-metric-hint {{
    font-size: .74rem; color: var(--cc-hint); margin-top: .38rem; font-weight: 500;
}}

/* Dark headline surface (matte near-black) */
.cc-metric-card.cc-dark {{
    background: var(--cc-ink); border-color: var(--cc-ink);
    box-shadow: 0 1px 2px rgba(11,18,32,.2), 0 18px 40px -22px rgba(11,18,32,.55);
}}
.cc-metric-card.cc-dark .cc-metric-value {{ color: #FFFFFF; }}
.cc-metric-card.cc-dark .cc-metric-label {{ color: #93A3BF; }}
.cc-metric-card.cc-dark .cc-metric-hint {{ color: #9DB8F7; }}

/* ---------- Status chips ---------- */
.cc-chip {{
    display: inline-block; font-size: .72rem; font-weight: 600;
    padding: .26rem .72rem; border-radius: 999px; margin-right: .45rem;
    border: 1px solid var(--cc-border); color: #475569; background: #FFFFFF;
    letter-spacing: .01em;
}}
.cc-chip-blue {{ color: var(--cc-blue-deep); border-color: #D6E2FB; background: var(--cc-blue-tint); }}
.cc-chip-green {{ color: #15803D; border-color: #D1F4DF; background: #F2FCF5; }}
.cc-chip-dark {{ color: #FFFFFF; background: var(--cc-ink); border-color: var(--cc-ink); }}

/* ---------- Section panels (matte insight cards) ---------- */
.cc-panel {{
    background: #FFFFFF;
    border: 1px solid var(--cc-border);
    border-radius: 14px;
    padding: 1.05rem 1.3rem;
    box-shadow: var(--cc-shadow-matte);
    margin-bottom: .5rem;
}}
.cc-panel-title {{
    font-weight: 700; color: var(--cc-ink); margin-bottom: .25rem; font-size: .95rem;
}}

/* ---------- Buttons ---------- */
.stButton > button {{
    border-radius: 9px; font-weight: 600; letter-spacing: .01em;
    transition: all .15s ease;
}}
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {{
    background: var(--cc-blue); color: #FFFFFF; border: 1px solid var(--cc-blue);
    box-shadow: 0 1px 2px rgba(37,99,235,.35);
}}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="baseButton-primary"]:hover {{
    background: var(--cc-blue-deep); border-color: var(--cc-blue-deep);
}}
.stButton > button[kind="secondary"],
.stButton > button[data-testid="baseButton-secondary"] {{
    background: #FFFFFF; color: var(--cc-ink); border: 1px solid #CBD5E1;
}}
.stButton > button[kind="secondary"]:hover,
.stButton > button[data-testid="baseButton-secondary"]:hover {{
    background: var(--cc-bg-soft); border-color: var(--cc-border-strong); color: var(--cc-ink);
}}

/* ---------- Radio groups (navigation + model selector) ---------- */
div[role="radiogroup"] > label {{
    display: flex; align-items: center;
    padding: .52rem .72rem; margin: .12rem 0; border-radius: 9px;
    border: 1px solid transparent; color: #334155; font-weight: 500;
    cursor: pointer; transition: all .15s ease;
    width: fit-content; min-width: 55%;
}}
div[role="radiogroup"] > label:hover {{ background: #F1F5F9; }}
div[role="radiogroup"] > label:has(input:checked) {{
    background: var(--cc-blue-tint); border-color: #D6E2FB;
    color: var(--cc-blue-deep); font-weight: 600;
}}

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {{
    background: #FBFCFE; border-right: 1px solid var(--cc-border);
}}
section[data-testid="stSidebar"] .block-container {{ padding-top: 1.4rem; }}

/* ---------- Alerts: neutral matte, blue accent edge ---------- */
[data-testid="stAlert"] {{
    background: var(--cc-bg-soft); color: #334155;
    border: 1px solid var(--cc-border); border-left: 3px solid var(--cc-blue);
    border-radius: 12px; box-shadow: var(--cc-shadow-matte);
}}
[data-testid="stAlert"] p {{ color: #334155; }}

/* ---------- Expanders ---------- */
[data-testid="stExpander"] {{
    border: 1px solid var(--cc-border); border-radius: 12px;
    background: #FFFFFF; box-shadow: var(--cc-shadow-matte); overflow: hidden;
}}
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary p {{ color: var(--cc-text); font-weight: 600; }}
[data-testid="stExpander"] summary:hover span,
[data-testid="stExpander"] summary:hover p {{ color: var(--cc-blue-deep); }}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {{ gap: 2px; border-bottom: 1px solid var(--cc-border); }}
.stTabs [data-baseweb="tab"] {{ border-radius: 9px 9px 0 0; font-weight: 600; color: var(--cc-muted); }}
.stTabs [data-baseweb="tab"]:hover {{ color: var(--cc-text); background: var(--cc-bg-soft); }}
.stTabs [aria-selected="true"] {{ color: var(--cc-blue-deep) !important; }}
.stTabs [data-baseweb="tab-highlight"] {{ background: var(--cc-blue); height: 2px; }}

/* ---------- Inputs ---------- */
.stSlider label, .stCheckbox label, .stSelectbox label, .stRadio label {{
    color: var(--cc-text); font-weight: 600; font-size: .88rem;
}}
.stSlider label p, .stCheckbox label p {{ color: var(--cc-muted); font-weight: 400; }}

/* ---------- Bounded containers (control areas) ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {{
    background: #FFFFFF;
    border: 1px solid var(--cc-border) !important;
    border-radius: 14px !important;
    box-shadow: var(--cc-shadow-matte);
    padding-top: 1rem; padding-bottom: .4rem;
}}

/* ---------- Dataframe / tables ---------- */
[data-testid="stDataFrame"] {{ border: 1px solid var(--cc-border); border-radius: 12px; overflow: hidden; }}

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar {{ width: 9px; height: 9px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: #CBD5E1; border-radius: 999px; border: 2px solid #FFF; }}
::-webkit-scrollbar-thumb:hover {{ background: #94A3B8; }}
</style>
"""


def inject_css() -> None:
    """Apply the shared design system once per run."""
    st.markdown(_APP_CSS, unsafe_allow_html=True)


def page_header(title: str, description: str) -> None:
    """Consistent page pattern: one heading plus a one-line description."""
    st.markdown(f"## {title}")
    st.markdown(
        f"<p class='cc-note' style='margin-top:-0.55rem; margin-bottom:1.1rem'>{description}</p>",
        unsafe_allow_html=True,
    )


def metric_card(
    label: str,
    value: str,
    hint: str | None = None,
    dark: bool = False,
) -> str:
    """Return metric-card HTML; caller places it via st.markdown in columns."""
    cls = "cc-metric-card cc-dark" if dark else "cc-metric-card"
    hint_html = f"<div class='cc-metric-hint'>{hint}</div>" if hint else ""
    return (
        f"<div class='{cls}'>"
        f"<div class='cc-metric-label'>{label}</div>"
        f"<div class='cc-metric-value'>{value}</div>"
        f"{hint_html}"
        f"</div>"
    )


def metric_row(cards: list[dict]) -> None:
    """Render 1-5 metric cards in a responsive row of columns."""
    cols = st.columns(max(len(cards), 1), gap="small")
    for col, card in zip(cols, cards):
        with col:
            st.markdown(metric_card(**card), unsafe_allow_html=True)


def status_chip(text: str, tone: str = "neutral") -> None:
    """Small inline status chip (dataset loaded, split label, threshold...)."""
    st.markdown(f"<span class='cc-chip cc-chip-{tone}'>{text}</span>", unsafe_allow_html=True)


def status_chip_row(chips: list[tuple[str, str]]) -> None:
    """Render several chips on one line."""
    html = "".join(
        f"<span class='cc-chip cc-chip-{tone}'>{text}</span>" for text, tone in chips
    )
    st.markdown(html, unsafe_allow_html=True)
