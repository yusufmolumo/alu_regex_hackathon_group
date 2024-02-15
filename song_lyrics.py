import re

api_response = """

Song Lyrics: "[Verse 1] Some lyrics here", "[Verse 2] Another set of lyrics"
"""

song_lyrics_pattern = r'"\[Verse (\d+)\] (.+?)"'
song_lyrics = re.findall(song_lyrics_pattern, api_response)

print("Song Lyrics:", song_lyrics)
