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
    page_icon="🫠",
    page_title="F1 Custom Points System TESTING",
    # icon=":material/sports_motorsports:",
    # layout="wide",
    menu_items={
        # "Get Help": "",
        # 'Report a bug': "",
        "About": "This app allows you to simulate the F1 season with a custom points system.",
    },
)


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


# VARIABLES -------------------------------------------------------------------

# CONSTANTS -------------------------------------------------------------------

pts_all = {
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

## race points
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


## sprint points

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

# FUNCTIONS -------------------------------------------------------------------

## custom points systems functions

max_f1_cars = 22


def set_race_points(race_pts_dict: dict = None):

    if race_pts_dict:
        # set the values
        for i, value in race_pts_dict.items():
            st.session_state[f"rp{i}"] = value
        # set the rest to 0
        for i in [
            x for x in range(1, max_f1_cars + 1) if x not in race_pts_dict.keys()
        ]:
            st.session_state[f"rp{i}"] = 0

    else:
        # set all to 0
        for i in range(1, max_f1_cars + 1):
            st.session_state[f"rp{i}"] = 0


def set_sprint_points(sprint_pts_dict: dict = None):
    if sprint_pts_dict:
        # set the values
        for i, value in sprint_pts_dict.items():
            st.session_state[f"sp{i}"] = value
        # set the rest to 0
        for i in [
            x for x in range(1, max_f1_cars + 1) if x not in sprint_pts_dict.keys()
        ]:
            st.session_state[f"sp{i}"] = 0

    else:
        # set all to 0
        for i in range(1, max_f1_cars + 1):
            st.session_state[f"sp{i}"] = 0


def set_points_system(
    race_pts_dict: dict = None,
    fastest_lap_toggle: bool = None,
    fastest_lap_points: int = None,
    eligible_positions: list = None,
    all_races_toggle: bool = None,
    top_n_count: list = None,
    split_season: bool = None,
    split_point: int = None,
    first_part_top_n_count: int = None,
    second_part_top_n_count: int = None,
    last_race_toggle: bool = None,
    last_race_points_multiple: int = None,
    sprint_races_toggle: bool = None,
    sprint_pts_dict: dict = None,
):

    # race points
    if race_pts_dict != None:
        set_race_points(race_pts_dict)

    # fastest lap
    if fastest_lap_toggle != None:
        st.session_state["fastest_lap_toggle"] = fastest_lap_toggle
    if fastest_lap_points != None:
        st.session_state["fastest_lap_points"] = fastest_lap_points
    if eligible_positions != None:
        st.session_state["eligible_positions"] = eligible_positions

    # all races count
    if all_races_toggle != None:
        st.session_state["all_races_toggle"] = all_races_toggle
    if top_n_count != None:
        st.session_state["top_n_count"] = top_n_count

    ## split season
    if split_season != None:
        st.session_state["split_season"] = split_season
    if split_point != None:
        st.session_state["split_point"] = split_point
    if first_part_top_n_count != None:
        st.session_state["first_part_top_n_count"] = first_part_top_n_count
    if second_part_top_n_count != None:
        st.session_state["second_part_top_n_count"] = second_part_top_n_count

    # last_race_toggle
    if last_race_toggle != None:
        st.session_state["last_race_toggle"] = last_race_toggle
    if last_race_points_multiple != None:
        st.session_state["last_race_points_multiple"] = last_race_points_multiple

    # sprint points
    if sprint_races_toggle != None:
        st.session_state["sprint_races_toggle"] = sprint_races_toggle
    if sprint_pts_dict != None:
        set_sprint_points(sprint_pts_dict)


# SESSION STATE ----------------------------------------------------------------


@st.cache_resource
def set_session_state():
    for i in range(1, max_f1_cars + 1):
        if f"rp{i}" not in st.session_state:
            st.session_state[f"rp{i}"] = 0
        if f"sp{i}" not in st.session_state:
            st.session_state[f"sp{i}"] = 0

        #
        st.session_state["fastest_lap_toggle"] = True
        st.session_state["fastest_lap_points"] = 1
        st.session_state["eligible_positions"] = [1, max_f1_cars]

        st.session_state["all_races_toggle"] = True
        st.session_state["top_n_count"] = [1, 1]

        st.session_state["last_race_toggle"] = True
        st.session_state["last_race_points_multiple"] = 1

        st.session_state["sprint_races_toggle"] = True


# set_session_state()

# PAGE CONTENT ----------------------------------------------------------------


# header
icon("🫠")
st.title("F1 Custom Points System")


st.markdown("## Presets")
with st.container():
    st.markdown("### :red[Random]")
    if st.button("All", use_container_width=True, key="points_all"):
        set_points_system(
            race_pts_dict=pts_all,
            fastest_lap_toggle=True,
            fastest_lap_points=1,
            eligible_positions=[1, max_f1_cars],
            all_races_toggle=True,
            top_n_count=[1, 24],
            last_race_toggle=True,
            last_race_points_multiple=1,
            sprint_races_toggle=True,
            sprint_pts_dict=pts_all,
        )

with st.container():
    st.markdown("### :red[Sprint]")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("**PRESENT**", use_container_width=True, key="present_all"):
            set_points_system(
                race_pts_dict=race_pts_2010,
                fastest_lap_toggle=True,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=True,
                sprint_pts_dict=sprint_pts_2022,
            )
    with c2:
        if st.button("2021", use_container_width=True, key="2021_all"):
            set_points_system(
                race_pts_dict=race_pts_2010,
                fastest_lap_toggle=True,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=True,
                sprint_pts_dict=sprint_pts_2021,
            )

with st.container():
    st.markdown("### :red[Through the Ages]")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.button("2010-2018", use_container_width=True, key="2010_all"):
            set_points_system(
                race_pts_dict=race_pts_2010,
                fastest_lap_toggle=False,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=False,
                sprint_pts_dict={},
            )
    with c2:
        if st.button(
            "2014",
            use_container_width=True,
            key="2014_all",
            help="Double points last race",
        ):
            set_points_system(
                race_pts_dict=race_pts_2010,
                fastest_lap_toggle=False,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=True,
                last_race_points_multiple=2,
                sprint_races_toggle=False,
                sprint_pts_dict={},
            )
    with c3:
        if st.button("2003-2009", use_container_width=True, key="2003_all"):
            set_points_system(
                race_pts_dict=race_pts_2003,
                fastest_lap_toggle=False,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=False,
                sprint_pts_dict={},
            )
    with c4:
        if st.button("1991-2002", use_container_width=True, key="1991_all"):
            set_points_system(
                race_pts_dict=race_pts_1991,
                fastest_lap_toggle=False,
                fastest_lap_points=1,
                eligible_positions=[1, 10],
                all_races_toggle=True,
                top_n_count=[1, 24],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=False,
                sprint_pts_dict={},
            )

    with c5:
        if st.button("1981-1990", use_container_width=True, key="1981_all"):
            set_points_system(
                race_pts_dict=race_pts_1991,
                fastest_lap_toggle=False,
                fastest_lap_points=0,
                eligible_positions=[1, 10],
                all_races_toggle=False,
                split_season=False,
                top_n_count=[1, 11],
                last_race_toggle=False,
                last_race_points_multiple=1,
                sprint_races_toggle=False,
                sprint_pts_dict={},
            )


## custom points system
st.markdown("## Points System")

### race points

with st.container(border=True):
    st.markdown("### :red[Race Points]")

    with st.container():
        c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

        # preset buttons
        with c1:
            if st.button(
                "All",
                key="race_all",
                use_container_width=True,
                help="Every position gets points",
            ):
                set_race_points(race_pts_dict=pts_all)
        with c2:
            if st.button("Present", use_container_width=True, help="2010-PRESENT"):
                set_race_points(race_pts_dict=race_pts_2010)
        with c3:
            if st.button("2003", use_container_width=True, help="2003-2009"):
                set_race_points(race_pts_dict=race_pts_2003)
        with c4:
            if st.button("1991", use_container_width=True, help="1991-2002"):
                set_race_points(race_pts_dict=race_pts_1991)

        with c5:
            if st.button("1962", use_container_width=True, help="1962-1990"):
                set_race_points(race_pts_dict=race_pts_1962)
        with c7:
            if st.button(
                "**Reset**",
                use_container_width=True,
                help="Reset all points to 0",
                type="primary",
                key="race_reset",
            ):
                set_race_points()

    with st.container():
        with st.container():
            P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 = st.columns(10)
            with P1:
                rp1 = st.number_input("P1", step=1, key="rp1")
            with P2:
                rp2 = st.number_input("P2", step=1, key="rp2")
            with P3:
                rp3 = st.number_input("P3", step=1, key="rp3")
            with P4:
                rp4 = st.number_input("P4", step=1, key="rp4")
            with P5:
                rp5 = st.number_input("P5", step=1, key="rp5")
            with P6:
                rp6 = st.number_input("P6", step=1, key="rp6")
            with P7:
                rp7 = st.number_input("P7", step=1, key="rp7")
            with P8:
                rp8 = st.number_input("P8", step=1, key="rp8")
            with P9:
                rp9 = st.number_input("P9", step=1, key="rp9")
            with P10:
                rp10 = st.number_input("P10", step=1, key="rp10")

        with st.container():
            P11, P12, P13, P14, P15, P16, P17, P18, P19, P20 = st.columns(10)
            with P11:
                rp11 = st.number_input("P11", step=1, key="rp11")
            with P12:
                rp12 = st.number_input("P12", step=1, key="rp12")
            with P13:
                rp13 = st.number_input("P13", step=1, key="rp13")
            with P14:
                rp14 = st.number_input("P14", step=1, key="rp14")
            with P15:
                rp15 = st.number_input("P15", step=1, key="rp15")
            with P16:
                rp16 = st.number_input("P16", step=1, key="rp16")
            with P17:
                rp17 = st.number_input("P17", step=1, key="rp17")
            with P18:
                rp18 = st.number_input("P18", step=1, key="rp18")
            with P19:
                rp19 = st.number_input("P19", step=1, key="rp19")
            with P20:
                rp20 = st.number_input("P20", step=1, key="rp20")

    ### fastest lap points

    with st.container():
        c1, c2 = st.columns([0.35, 0.65])
        with c1:
            st.markdown("#### Fastest Lap Points")

        with c2:
            fastest_lap_toggle = st.toggle("Fastest Lap", key="fastest_lap_toggle")

    ### fastest lap
    if fastest_lap_toggle:
        with st.container():
            fastest_points, fastest_positions = st.columns(2)
            with fastest_points:
                fastest_lap_points = st.number_input(
                    "Points", key="fastest_lap_points", step=1
                )
            with fastest_positions:
                eligible_positions = st.slider(
                    "Eligible Positions",
                    key="eligible_positions",
                    min_value=1,
                    max_value=max_f1_cars,
                    value=[1, max_f1_cars],
                )

    ### all races count

    with st.container():
        c1, c2 = st.columns([0.35, 0.65])
        with c1:
            st.markdown("#### All Races Count")
        with c2:
            all_races_toggle = st.toggle(
                "All races count towards championship", key="all_races_toggle"
            )

        if not all_races_toggle:

            split_season = st.toggle("split season", key="split_season")

            if split_season:

                with st.container():
                    c1, c2 = st.columns([0.2, 0.8])
                    with c1:

                        split_half = st.checkbox("Split Half", key="split_half")
                        if split_half:
                            st.session_state["split_point"] = 12

                    with c2:
                        split_point = st.slider(
                            "Split Point",
                            key="split_point",
                            min_value=1,
                            max_value=24,
                            disabled=split_half,
                        )

                with st.container():
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write("First Half")

                        first_part_top_n_count = st.slider(
                            "Top n count towards championship",
                            key="first_part_top_n_count",
                            min_value=1,
                            max_value=24,
                            value=st.session_state["split_point"],
                            disabled=False,
                        )

                    with c2:
                        st.write("Second Half")
                    with c2:
                        second_part_top_n_count = st.slider(
                            "Top n count towards championship",
                            key="second_part_top_n_count",
                            min_value=1,
                            max_value=24,
                            value=st.session_state["split_point"],
                            disabled=False,
                        )

            else:
                top_n_count = st.slider(
                    "Top n count towards championship",
                    key="top_n_count",
                    min_value=1,
                    max_value=24,
                    disabled=False,
                )

    ### last race points
    with st.container():
        c1, c2 = st.columns([0.35, 0.65])
        with c1:
            st.markdown("#### Last Race Points Multiplier")
        with c2:
            last_race_toggle = st.toggle(
                "Last race points multiplier",
                key="last_race_toggle",
                value=False,
                help="2014 the last race was double points",
            )

    with st.container():
        if last_race_toggle:
            last_race_points_multiple = st.number_input(
                "Points Multiplier", value=2, key="last_race_points_multiple"
            )

        else:
            last_race_points_multiple = 1

## sprint points

with st.container(border=True):
    with st.container():
        c1, c2 = st.columns([0.35, 0.65])
        with c1:
            st.markdown("### :red[Sprint Points]")
        with c2:
            sprint_races_toggle = st.toggle(
                "Sprint races count towards championship",
                key="sprint_races_toggle",
            )

    if sprint_races_toggle:
        with st.container():

            with st.container():
                c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

                with c1:
                    if st.button(
                        "All",
                        key="sprint_all",
                        use_container_width=True,
                        help="Every position gets points",
                    ):
                        set_sprint_points(sprint_pts_dict=pts_all)
                with c2:
                    if st.button(
                        "Present", use_container_width=True, help="2022-PRESENT"
                    ):
                        set_sprint_points(sprint_pts_dict=sprint_pts_2022)

                with c3:
                    if st.button("2021", use_container_width=True, help="2021"):
                        set_sprint_points(sprint_pts_dict=sprint_pts_2021)

                with c7:
                    if st.button(
                        "**Reset**",
                        use_container_width=True,
                        help="Reset all points to 0",
                        type="primary",
                        key="sprint_reset",
                    ):
                        set_sprint_points()

            with st.container():
                with st.container():
                    P1, P2, P3, P4, P5, P6, P7, P8, P9, P10 = st.columns(10)
                    with P1:
                        sp1 = st.number_input("P1", step=1, key="sp1")
                    with P2:
                        sp2 = st.number_input("P2", step=1, key="sp2")
                    with P3:
                        sp3 = st.number_input("P3", step=1, key="sp3")
                    with P4:
                        sp4 = st.number_input("P4", step=1, key="sp4")
                    with P5:
                        sp5 = st.number_input("P5", step=1, key="sp5")
                    with P6:
                        sp6 = st.number_input("P6", step=1, key="sp6")
                    with P7:
                        sp7 = st.number_input("P7", step=1, key="sp7")
                    with P8:
                        sp8 = st.number_input("P8", step=1, key="sp8")
                    with P9:
                        sp9 = st.number_input("P9", step=1, key="sp9")
                    with P10:
                        sp10 = st.number_input("P10", step=1, key="sp10")

                with st.container():
                    P11, P12, P13, P14, P15, P16, P17, P18, P19, P20 = st.columns(10)
                    with P11:
                        sp11 = st.number_input("P11", step=1, key="sp11")
                    with P12:
                        sp12 = st.number_input("P12", step=1, key="sp12")
                    with P13:
                        sp13 = st.number_input("P13", step=1, key="sp13")
                    with P14:
                        sp14 = st.number_input("P14", step=1, key="sp14")
                    with P15:
                        sp15 = st.number_input("P15", step=1, key="sp15")
                    with P16:
                        sp16 = st.number_input("P16", step=1, key="sp16")
                    with P17:
                        sp17 = st.number_input("P17", step=1, key="sp17")
                    with P18:
                        sp18 = st.number_input("P18", step=1, key="sp18")
                    with P19:
                        sp19 = st.number_input("P19", step=1, key="sp19")
                    with P20:
                        sp20 = st.number_input("P20", step=1, key="sp20")


st.markdown("---")
