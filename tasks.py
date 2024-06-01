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
            expected_output="""A list of top news story about the topic provided with  titles, URLs, and a brief summary for each story. 
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



        def analyse_content(self, agent, context):
            return Task(
                description=dedent(
                    f"""Analyse Each content and ensure analysed content should be well formatted.  Find out 4 sub topics in which we can divide content and then format article containing four sub topics.Also each article should contain conclusion in the end   """
                ),
                agent=agent,
                context=context,
                expected_output="""A markdown-formatted analysis for each content, including 4 subtopic 
                    Example Output: 
                    '## AI takes spotlight in Super Bowl commercials\n\n
                    **Selected Subtopic 1:
                    ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                    **Selected Subtopic 2:
                    ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                    **Selected Subtopic 3:
                    - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                    **Selected Subtopic 4:
                    - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                    **Conclusion :** While AI-related ads have been rampant over the last year, its Super Bowl presence is a big mainstream moment.\n\n'
                """
            )  

        def compile_blog(self, agent, context):
            return Task(
                description=dedent(
                    f"""Compile all content to create a blog   """
                ),
                agent=agent,
                context=context,
                expected_output=f"""A complete blog in markdown format, with a consistent style and layout.
                    Example Output: 
                    {query}
                    ## List of subheadings
                        *Selected Subtopic 1:
                        *Selected Subtopic 2:
                        *Selected Subtopic 3:
                        *Selected Subtopic 4:
                    '## AI takes spotlight in Super Bowl commercials\n\n
                    **Selected Subtopic 1:
                    ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                    **Selected Subtopic 2:
                    ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                    **Selected Subtopic 3:
                    - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                    **Selected Subtopic 4:
                    - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                    **Conclusion :** While AI-related ads have been rampant over the last year, its Super Bowl presence is a big mainstream moment.\n\n'
                """
            )  
