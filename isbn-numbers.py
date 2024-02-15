import re

api_response = """

ISBN Numbers: "ISBN 123-4-567-89012-3", "ISBN 987-6-543-21098-7"
"""

isbn_number_pattern = r'"ISBN (\d{3}-\d-\d{3}-\d{5}-\d)"'
isbn_numbers = re.findall(isbn_number_pattern, api_response)

print("ISBN Numbers:", isbn_numbers)
