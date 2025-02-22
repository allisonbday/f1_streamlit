# IMPORTS ---------------------------------------------------------------------
import os
import streamlit as st
from PIL import Image
from datetime import date, timedelta

# import from src
path = os.path.dirname(__file__)
# from src.open_meto_api import OpenMeteoAPI

# PAGE SET UP -----------------------------------------------------------------

st.set_page_config(
    page_icon=":house:",
    page_title="Allison's RaceCraft Analytics",
    menu_items={
        # "Get Help": "",
        # 'Report a bug': "",
        "About": "This app allows you to simulate the F1 season with a custom points system.",
    },
)  # , layout="wide")

# st.navigation()


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon("🏎️")
st.title("Allison's RaceCraft Analytics")
