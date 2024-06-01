from crewai import Agent
from textwrap import dedent
#from langchain.llms import 
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI 
import os,dotenv
from tools import customTools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
dotenv.load_dotenv()

class CustomAgents:
    llm = None  
    def __init__(self):
      self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                   verbose=True,
                                   temperature=0.5,
                                   google_api_key=os.getenv("GEMINI_API_KEY"))
      print ("Google LLM initialized")
      print(self.llm)
        

    def content_gatherer(self):
        return Agent(
            role="Senior Research Analyst",
            goal=dedent(f"""Go through a detailed search to find and analyst latest updates on the topic provided"""),
            backstory=dedent(f"""You have 10 years of experience of researching on topics. you explore latest technologies and development for the topic provided."""),
            
            tools=[customTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

   
