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
            role="Content Researcher",
            goal=dedent("""Find latest news or updates on the topic provided"""),
            backstory=dedent(f"""You have 20 years of experience of researching on topics. you explore latest technologies and development for the topic provided."""),
            
            tools=[customTools.search_internet],
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
        )
    

    def analyse_content(self):
        return Agent(
            role="Senior Analyst",
            goal=dedent(f"""Go through each content,analyse and generate a detailed markdown report on the topic provided"""),
            backstory=dedent(f"""With a critical eye and a knack for distilling complex information, you provide deep insightful
            analyses for the topic provided.if required you can provide comparison of products or services"""),
            
            tools=[customTools.search_internet],
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
        )

   
    def blog_writer(self):
        return Agent(
            role="Blog Content Compiler",

            goal=dedent(f"""Compile analysed content provided by senior Analyst into a final blog with markdown"""),

            backstory=dedent(f"""As a experienced content writer ,you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that captivates our readers. Make your to cover all points and a provide a conclusion in the end"""),
            verbose=True,
            llm=self.llm,
        )        
