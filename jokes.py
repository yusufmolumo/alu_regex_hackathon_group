import re

api_response = """

Jokes: "Why did the chicken cross the road? Because it wanted to get to the other side."
"""

joke_pattern = r'"Why did the (.+?) \? Because(.+?)"'
jokes = re.findall(joke_pattern, api_response)

print("Jokes:", jokes)
