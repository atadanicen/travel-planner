from datetime import datetime, timedelta

import streamlit as st

from main import TravelCrew

today = datetime.now()
one_year_from_now = today + timedelta(days=365)
seven_days_from_now = today + timedelta(days=7)

sidebar = st.sidebar

custom_css = """
<style>
    .st-emotion-cache-1g1z3k2 p {
        text-align:right;
    }
    .st-emotion-cache-k7vsyb h1{
        text-align:center;
        margin-top: -60px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

with sidebar:
    st.markdown(
        """
        # Travel Planner 🗺️
        ### *User Guide*
            1. Pick your dream destination
            2. Jot down what you love
            3. Send your details
            4. Bon voyage !!
        """
    )
    st.caption("Created by @atadanicen")
    st.divider()
    destination_city = st.text_input("Destination")
    interests = st.text_area("Write down your interests")

    dates = st.date_input(
        "Departure Time",
        (today, seven_days_from_now),
        today,
        one_year_from_now,
        format="DD/MM/YYYY",
    )


if len(dates) == 2 and destination_city and interests:
    start_date, end_date = dates
    travel_date = f"{start_date} to {end_date}"
    duration = (end_date - start_date).days
    col1, col2 = sidebar.columns(2)
    plan_journey = col1.button("Plan My Trip")

    if plan_journey:
        travel_crew = TravelCrew(destination_city, travel_date, interests, duration)
        with st.chat_message("assistant"):
            with st.status("🤖 Agents working on it...", expanded=True) as status:
                with st.container(height=500):
                    agent_outputs = travel_crew.run()
                    status.update(
                        label="Your Travel Plan is ready",
                        state="complete",
                        expanded=False,
                    )
        if len(agent_outputs) == 3:
            all_outputs = "\n".join(agent_outputs)
            col2.download_button("Download Plan", all_outputs)
