import ast

import streamlit as st
from langchain_core.agents import AgentAction


def streamlit_callback(step_output):
    """
    This function will be called after each step of the agent's execution.
    """
    for step in step_output:
        action, observations = step
        if isinstance(action, AgentAction):
            if action.tool != "_Exception":
                st.subheader("Action", divider="violet")
                st.json(action.json())
                if isinstance(observations, str):
                    try:
                        observation = ast.literal_eval(observations)
                        st.subheader("Observation", divider="violet")
                        st.json(observation)
                    except:
                        st.subheader("Observation", divider="violet")
                        st.write(observations)

        else:
            pass
