import streamlit as st
from crewai import Crew

from agents import TravelAgents
from tasks import TravelTasks
from utils import streamlit_callback


class TravelCrew:
    def __init__(self, destination_city, date_range, interests, duration):
        self.destination_city = destination_city
        self.interests = interests
        self.date_range = date_range
        self.duration = duration
        self.subheader = st.subheader(
            "Leave It to AI: Plan Your Perfect Vacation Hassle-Free",
            divider="violet",
            anchor=False,
        )
        self.travel_plan_placeholder = st.expander("Travel Plan", expanded=True)
        self.foodie_expander = st.expander("Foodie Agent Analysis")
        self.local_expert_expander = st.expander("Local Expert Analysis")

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        location_expert = agents.location_expert()
        local_foodie = agents.local_foodie()
        travel_concierge = agents.travel_concierge()

        gather_information_task = tasks.gather_information_task(
            location_expert,
            self.destination_city,
            self.date_range,
            self.interests,
        )

        foodie_task = tasks.foodie_task(
            local_foodie,
            self.destination_city,
        )
        context_task_list = [gather_information_task, foodie_task]

        plan_task = tasks.plan_task(
            travel_concierge,
            self.destination_city,
            self.date_range,
            self.duration,
            context_task_list,
        )

        crew = Crew(
            agents=[location_expert, local_foodie, travel_concierge],
            tasks=[gather_information_task, foodie_task, plan_task],
            verbose=True,
            step_callback=streamlit_callback,
        )

        travel_plan_output = crew.kickoff()
        gather_information_task_output = gather_information_task.output.raw_output
        foodie_task_output = foodie_task.output.raw_output

        self.travel_plan_placeholder.container(height=600, border=False).markdown(
            travel_plan_output
        )
        self.local_expert_expander.container(height=450, border=False).markdown(
            gather_information_task_output
        )
        self.foodie_expander.container(height=450, border=False).markdown(
            foodie_task_output
        )

        return [travel_plan_output, gather_information_task_output, foodie_task_output]
