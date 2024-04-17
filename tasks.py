from textwrap import dedent

from crewai import Task


class TravelTasks:
    def gather_information_task(self, agent, destination_city, date_range, interests):
        return Task(
            description=dedent(
                f"""
                Find things to do in {destination_city}.
                
                Find festivals and attractions between {date_range} in {destination_city}.
                Traveler Interests: {interests}
                
                Then analyze and make a list.
          """
            ),
            expected_output="Places to visit and explore. Must be formatted as list",
            agent=agent,
        )

    def foodie_task(self, agent, destination_city):
        return Task(
            description=dedent(
                f"""
            Find best local food spots in {destination_city}, 
            along with a list of must-try dishes and locations and make a list.

            """
            ),
            expected_output="Local foods and spots to try.Must be formatted as list",
            agent=agent,
        )

    def plan_task(self, agent, destination_city, date_range, duration, tasks_list):
        return Task(
            description=dedent(
                f"Using informations write {duration}-day plan formatted as list. Trip Date: {date_range}"
            ),
            context=tasks_list,
            expected_output=f"""{duration}-day trip plan to {destination_city} with detailed breakdown for each day. Must be formatted as list.""",
            agent=agent,
        )
