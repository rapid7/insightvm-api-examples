import os
from getpass import getpass
import requests
from requests.auth import HTTPBasicAuth

# Defaults: Change to suit your environment.
CONSOLE_URL = "https://put_console_IP_or_hostname_here:3780" # Example : https://example.rapid7.com:3780
ENDPOINT = "sites"
QUERY_PARAMS = ""    # Example : "size=5&page=10"
REQUEST_TIMEOUT = 90

url = f"{CONSOLE_URL}/api/3/{ENDPOINT}?{QUERY_PARAMS}"

# Optionally use environment variables or CLI input.
CONSOLE_USER = os.environ.get("CONSOLE_USER")
if CONSOLE_USER is None:
    CONSOLE_USER = input('Enter your username: ')
#
CONSOLE_PASS = os.environ.get("CONSOLE_PASS")
if CONSOLE_PASS is None:
    CONSOLE_PASS = getpass('Enter your password: ')
#
response = requests.get(
    url,
    auth=HTTPBasicAuth(CONSOLE_USER, CONSOLE_PASS),
    verify=False,   # For consoles with self-signed SSL certificates.
                    # Set to True if your SSL Cert is signed by a valid CA.
                    # Causes an InsecureRequestWarning when set to False.
    timeout=REQUEST_TIMEOUT
    )
#
print(response)
