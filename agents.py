from crewai import Agent
from textwrap import dedent
#from langchain.llms import 
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI 
import os,dotenv


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
dotenv.load_dotenv()

class CustomAgents:
    llm = None  
    def __init__(self):
      llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                   verbose=True,
                                   temperature=0.5,
                                   google_api_key=os.getenv("GEMINI_API_KEY"))
        

    def agent_1_name(self):
        return Agent(
            role="Define agent 1 role here",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""Define agent 1 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
