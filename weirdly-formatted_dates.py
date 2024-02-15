import re

api_response = """

Weirdly Formatted Dates: "12-Feb-2023", "21-Oct-2010"
"""

weird_date_pattern = r'"\d{2}-[a-zA-Z]{3}-\d{4}"'
weird_dates = re.findall(weird_date_pattern, api_response)

print("Weirdly Formatted Dates:", weird_dates)
