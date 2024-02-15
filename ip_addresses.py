import re

api_response = """

IP Addresses: "192.168.0.1", "255.0.127.42"
"""

ip_address_pattern = r'"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"'
ip_addresses = re.findall(ip_address_pattern, api_response)

print("IP Addresses:", ip_addresses)
