from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()


@tool("Search information from the web")
def browser(query):
    """
    Search the web for informations
    example input:
    "{ "query": "things to do in Cappadocia for historical places" }"
    """
    search = GoogleSerperAPIWrapper()
    result = search.run(query)
    return result.replace("...", "").replace("\xa0", "")
