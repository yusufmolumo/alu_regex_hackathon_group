import re

api_response = """

TV Episode Titles: "Game of Thrones S03E05: The Bear and the Maiden Fair", "Stranger Things S02E03: The Pollywog"
"""

episode_title_pattern = r'"(.+?) S(\d{2})E(\d{2}): (.+?)"'
episode_titles = re.findall(episode_title_pattern, api_response)

print("TV Episode Titles:", episode_titles)
