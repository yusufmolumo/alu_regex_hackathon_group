import re

api_response = """

Movie Titles: "Inception (2010)", "The Shawshank Redemption (1994)", "La La Land (2016)"
"""

movie_title_pattern = r'"(.+?) \((\d{4})\)"'
movie_titles = re.findall(movie_title_pattern, api_response)

print("Movie Titles:", movie_titles)
