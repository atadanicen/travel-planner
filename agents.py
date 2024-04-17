from crewai import Agent
from langchain_community.llms import Ollama

from tools import browser


class TravelAgents:
    local_llm = Ollama(model="openhermes", temperature=0)

    def location_expert(self):
        """
        Initializes and returns an Agent object that represents a travel locations expert.

        Parameters:
            self (TravelAgents): The TravelAgents instance that the function is called on.

        Returns:
            Agent: An Agent object that represents a travel locations expert.

        """
        return Agent(
            role="Travel Locations Expert",
            goal="Help travelers to explore the cities.",
            backstory="""You are a professional guide with a passion for travel.
            An expert in analyzing travel data to finish the given task and has extensive knowledge about writing list""",
            tools=[browser],
            verbose=True,
            llm=TravelAgents.local_llm,
            allow_delegation=False,
        )

    def local_foodie(self):
        """
        Initializes and returns an Agent object that represents a foodie

        Parameters:
            self (TravelAgents): The TravelAgents instance that the function is called on.

        Returns:
            Agent: An Agent object that represents a foodie.
        """
        return Agent(
            role="Local Foodie",
            goal="Find the best local food",
            backstory="""You are a group of food enthusiasts who love to explore
            local cuisines of the city. You are always on the lookout for hidden gems
            and authentic dishes. Your knowledge always MUST be TRUE. and has extensive knowledge about writing list""",
            tools=[browser],
            verbose=True,
            llm=TravelAgents.local_llm,
            allow_delegation=False,
        )

    def travel_concierge(self):
        """
        Initializes and returns an Agent object that represents a travel concierge.

        Parameters:
            self (TravelAgents): The TravelAgents instance that the function is called on.

        Returns:
            Agent: An Agent object that represents a travel concierge.
        """
        return Agent(
            role="Travel Planner",
            goal="Write a detailed travel itinerary formatted as list.",
            backstory="""Great planner with extensive knowledge about needs of the traveler and has extensive knowledge about writing list.""",
            verbose=True,
            allow_delegation=False,
            llm=TravelAgents.local_llm,
        )
