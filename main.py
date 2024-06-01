import os
from crewai import Agent, Task, Crew, Process
#from langchain_openai import ChatOpenAI
#from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

#from langchain.tools import DuckDuckGoSearchRun

#search_tool = DuckDuckGoSearchRun()

#os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
#os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, query):
        self.query = query

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        content_gatherer = agents.content_gatherer()
        #custom_agent_2 = agents.agent_2_name()

        # Custom tasks include agent name and variables as input
        find_content = tasks.find_content(
            content_gatherer,
            self.query
        )

      #  custom_task_2 = tasks.task_2_name(
      #      custom_agent_2,
      #  )

        # Define your custom crew here
        crew = Crew(
            agents=[content_gatherer],
            tasks=[find_content],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    query = input(dedent("""Write topic for which you want a blog: """))
    #var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(query)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
