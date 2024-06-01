from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def find_content(self, agent, query):
        return Task(
            description=dedent(
                f"""Fetch latest content about the topic provided. try to provide current information. try to gather information from different companies or websites. Find websites and content which explain the topic. if query is asking for top products find websites or content which provide product list according to query
                    Topic provided to do research is : {query}
        """
            ),
            agent=agent,
            expected_output="""A list of top news story about the topic provided with  titles, URLs, and a brief summary for each story from the past 7days. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
        )  
