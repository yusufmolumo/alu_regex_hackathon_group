import re

api_response = """

Hex Color Codes: "#FF4500", "#00FFFF"
"""

hex_color_code_pattern = r'"#([a-fA-F0-9]{6})"'
hex_color_codes = re.findall(hex_color_code_pattern, api_response)

print("Hex Color Codes:", hex_color_codes)
