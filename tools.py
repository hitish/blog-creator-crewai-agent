from dotenv import load_dotenv
load_dotenv()
import os
from langchain.tools import tool

from exa_py import Exa

# Initialize the tool for internet searching capabilities
class customTools:
    
    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        print("Searching the internet...")
        exa = Exa(api_key=os.environ['EXA_API_KEY'])
        response = exa.search_and_contents(f"{query}",type="neural", use_autoprompt=True, num_results=5,highlights=True)
        print(response)
        return response