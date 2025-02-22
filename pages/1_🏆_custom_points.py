# IMPORTS ---------------------------------------------------------------------
import os
import streamlit as st
from PIL import Image
from datetime import date, timedelta

import numpy as np
import pandas as pd

# import from src
path = os.path.dirname(__file__)
# from src.open_meto_api import OpenMeteoAPI

# PAGE SET UP -----------------------------------------------------------------

st.set_page_config(
    page_icon="🏆",
    page_title="F1 Custom Points System",
    # icon=":material/sports_motorsports:",
    menu_items={
        # "Get Help": "",
        # 'Report a bug': "",
        "About": "This app allows you to simulate the F1 season with a custom points system.",
    },
)  # , layout="wide")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


# SESSION STATE ----------------------------------------------------------------

st.cache_resource()


def set_session_state():
    for i in range(1, 50):
        if f"rp{i}" not in st.session_state:
            st.session_state[f"rp{i}"] = 0
        if f"sp{i}" not in st.session_state:
            st.session_state[f"sp{i}"] = 0


set_session_state()


# FUNCTIONS -------------------------------------------------------------------

## custom points systems functions

max_f1_cars = 50


### all count


def set_all_races_count(all_count_bool: bool = True, top_n_count: int = 100):
    st.session_state["all_races_count"] = False
    st.session_state["top_n_count"] = top_n_count


### race points
def set_race_points(race_points_dict: dict = None):
    if race_points_dict:
        for i, value in race_points_dict.items():
            st.session_state[f"rp{i}"] = value

        for i in [x for x in range(1, 50) if x not in race_points_dict.keys()]:
            st.session_state[f"rp{i}"] = 0
        st.markdown("### Points per Position SET USING DICT")

    else:
        for i in range(1, 50):
            st.session_state[f"rp{i}"] = 0
        st.markdown("### Points per Position SET USING DEFAULT")


race_pts_2010 = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}

race_pts_2003 = {1: 10, 2: 8, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}

race_pts_1991 = {1: 10, 2: 6, 3: 4, 4: 3, 5: 2, 6: 1}

race_pts_1962 = {1: 9, 2: 6, 3: 4, 4: 3, 5: 2, 6: 1}

race_pts_all = {
    1: 20,
    2: 19,
    3: 18,
    4: 17,
    5: 16,
    6: 15,
    7: 14,
    8: 13,
    9: 12,
    10: 11,
    11: 10,
    12: 9,
    13: 8,
    14: 7,
    15: 6,
    16: 5,
    17: 4,
    18: 3,
    19: 2,
    20: 1,
}


### sprint points


def set_sprint_points(sprint_points_dict: dict = None):
    if sprint_points_dict:
        for key, value in sprint_points_dict.items():
            st.session_state[f"sp{key}"] = value
            # st.session_state.sp1 = value

        for i in [
            x for x in range(1, max_f1_cars) if x not in sprint_points_dict.keys()
        ]:
            st.session_state[f"sp{i}"] = 0
    else:
        for i in range(1, max_f1_cars):
            st.session_state[f"sp{i}"] = 0


sprint_pts_2022 = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1,
}

sprint_pts_2021 = {1: 3, 2: 2, 3: 1}

sprint_pts_all = {
    1: 20,
    2: 19,
    3: 18,
    4: 17,
    5: 16,
    6: 15,
    7: 14,
    8: 13,
    9: 12,
    10: 11,
    11: 10,
    12: 9,
    13: 8,
    14: 7,
    15: 6,
    16: 5,
    17: 4,
    18: 3,
    19: 2,
    20: 1,
}


@st.cache_resource
def set_points_system(
    all_count_bool=True,
    top_n_count=100,
    race_points_dict: dict = None,
    sprint_points_dict: dict = None,
):
    set_all_races_count(all_count_bool, top_n_count)
    set_race_points(race_points_dict)
    set_sprint_points(sprint_points_dict)


# set_points_system(
#     all_count_bool=False,
#     top_n_count=20,
#     race_points_dict=race_pts_all,
#     sprint_points_dict=sprint_pts_2021,
# )


# PAGE CONTENT ----------------------------------------------------------------


# header
icon("🏆")
st.title("F1 Custom Points System")


# content
st.markdown(
    """
    This app allows you to simulate the F1 season with a custom points system.
    
    all the data comes from the [Ergast Developer API](http://ergast.com/mrd/).
    """
)

# custom points system
## normal races

st.markdown("## Custom Points System")


if st.button("2010 Points"):
    set_points_system(race_points_dict=race_pts_2010)

if st.button("Zero Points"):
    set_points_system()


# races count

st.markdown("### All races count towards championship")

all_races_count = st.toggle("All races count towards championship", value=True)

if not all_races_count:
    with st.container():
        top_n_count = st.number_input("Top n count towards championship", value=20)


### positions
st.markdown("### Points per Position")

with st.container():
    with st.container():
        P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 = st.columns(10)
        with P1:
            rp1_points = st.number_input("1st", value=st.session_state["rp1"])
        with P2:
            rp2_points = st.number_input("2nd", value=st.session_state["rp2"])
        with P3:
            rp3_points = st.number_input("3rd", value=st.session_state["rp3"])
        with P4:
            rp4_points = st.number_input("4th", value=st.session_state["rp4"])
        with P5:
            rp5_points = st.number_input("5th", value=st.session_state["rp5"])
        with P6:
            rp6_points = st.number_input("6th", value=st.session_state["rp6"])
        with P7:
            rp7_points = st.number_input("7th", value=st.session_state["rp7"])
        with P8:
            rp8_points = st.number_input("8th", value=st.session_state["rp8"])
        with P9:
            rp9_points = st.number_input("9th", value=st.session_state["rp9"])
        with P10:
            rp10_points = st.number_input("10th", value=st.session_state["rp10"])

    with st.container():
        P11, P12, P13, P14, P15, P16, P17, P18, P19, P20 = st.columns(10)
        with P11:
            rp11_points = st.number_input("11th", value=st.session_state["rp11"])
        with P12:
            rp12_points = st.number_input("12th", value=st.session_state["rp12"])
        with P13:
            rp13_points = st.number_input("13th", value=st.session_state["rp13"])
        with P14:
            rp14_points = st.number_input("14th", value=st.session_state["rp14"])
        with P15:
            rp15_points = st.number_input("15th", value=st.session_state["rp15"])
        with P16:
            rp16_points = st.number_input("16th", value=st.session_state["rp16"])
        with P17:
            rp17_points = st.number_input("17th", value=st.session_state["rp17"])
        with P18:
            rp18_points = st.number_input("18th", value=st.session_state["rp18"])
        with P19:
            rp19_points = st.number_input("19th", value=st.session_state["rp19"])
        with P20:
            rp20_points = st.number_input("20th", value=st.session_state["rp20"])


st.write(st.session_state)

### fastest lap

st.markdown("### Fastest Lap Points")

with st.container():
    fatest_lap_point = st.toggle("Fastest Lap", value=True)
    if fatest_lap_point:
        with st.container():
            fastest_points, fastest_positions = st.columns(2)
            with fastest_points:
                fastest_lap_points = st.number_input("Points", value=1)
            with fastest_positions:
                eligible_positions = st.slider(
                    "Eligible Positions", value=10, max_value=25
                )

    else:
        fastest_lap_points = 0

### last race points

st.markdown("### Last Race Special Points")

with st.container():
    last_race_points = st.toggle(
        "Last Race Special Points",
        value=False,
        help="2014 the last race was double points",
    )
    with st.container():
        if last_race_points:
            last_race_points_multiple = st.number_input("Points Multiplier", value=2)

        else:
            last_race_points_multiple = 1

## sprint races

sprint_races_count = st.toggle("Sprint races count towards championship", value=True)

if sprint_races_count:
    with st.container():

        (
            sprint_2022,
            sprint_2021,
            sprint_all_points,
        ) = st.columns(3)

        with sprint_2022:

            #     sprint_2022_points_rules = st.button(
            #         "2022 Sprint Rules",
            #         help="**PRESENT RULES**: positions 1-8 get points",
            #         on_click=set_sprint_points(sprint_points_dict=sprint_pts_2022),
            #     )

            def custom_function():
                st.session_state["sp1"] = 11111
                st.session_state["sp2"] = 11111

            sprint_2022_points_rules = st.button(
                "2022 Sprint Rules",
                help="positions 1-8 get points",
                on_click=custom_function(),
            )

        with sprint_2021:

            #     sprint_2021_points_rules = st.button(
            #         "2021 Sprint Rules",
            #         help="positions 1-3 get points",
            #         on_click=set_sprint_points(sprint_points_dict=sprint_pts_2021),
            #     )

            def custom_2():
                st.session_state["sp1"] = 99999
                st.session_state["sp2"] = 99999

            sprint_2021_points_rules = st.button(
                "2021 Sprint Rules",
                help="positions 1-3 get points",
                on_click=custom_2(),
            )

        with sprint_all_points:

            sprint_all = st.button(
                "All Sprint Points",
                help="positions 1-20 get points",
                on_click=set_sprint_points(sprint_points_dict=sprint_pts_all),
            )

        with st.container():
            SP1, SP2, SP3, SP4, SP5, SP6, SP7, SP8, SP9, SP10 = st.columns(10)
            with SP1:
                sp1_points = st.number_input("1st", value=0, key="sp1")
            with SP2:
                sp2_points = st.number_input("2nd", value=0, key="sp2")
            with SP3:
                sp3_points = st.number_input("3rd", value=0, key="sp3")
            with SP4:
                sp4_points = st.number_input("4th", value=0, key="sp4")
            with SP5:
                sp5_points = st.number_input("5th", value=0, key="sp5")
            with SP6:
                sp6_points = st.number_input("6th", value=0, key="sp6")
            with SP7:
                sp7_points = st.number_input("7th", value=0, key="sp7")
            with SP8:
                sp8_points = st.number_input("8th", value=0, key="sp8")
            with SP9:
                sp9_points = st.number_input("9th", value=0, key="sp9")
            with SP10:
                sp10_points = st.number_input("10th", value=0, key="sp10")
            SP11, SP12, SP13, SP14, SP15, SP16, SP17, SP18, SP19, SP20 = st.columns(10)
            with SP11:
                sp11_points = st.number_input("11th", value=0, key="sp11")
            with SP12:
                sp12_points = st.number_input("12th", value=0, key="sp12")
            with SP13:
                sp13_points = st.number_input("13th", value=0, key="sp13")
            with SP14:
                sp14_points = st.number_input("14th", value=0, key="sp14")
            with SP15:
                sp15_points = st.number_input("15th", value=0, key="sp15")
            with SP16:
                sp16_points = st.number_input("16th", value=0, key="sp16")
            with SP17:
                sp17_points = st.number_input("17th", value=0, key="sp17")
            with SP18:
                sp18_points = st.number_input("18th", value=0, key="sp18")
            with SP19:
                sp19_points = st.number_input("19th", value=0, key="sp19")
            with SP20:
                sp20_points = st.number_input("20th", value=0, key="sp20")


# import data

# results_2021 = pd.read_csv(path + r"\../data/results/results_2021.csv")

# results_2021
