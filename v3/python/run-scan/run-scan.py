#!/usr/bin/env python3
#
#  Description: Script that uses the Nexpose APIv3 to launch a scan of a specified site id

import json
from getpass import getpass

import urllib3
import requests
from requests.auth import HTTPBasicAuth

# Prompts to collect nexpose console and login information
host = input("Enter the server name (host) for InsightVM: ")
user = input("Enter your username: ")
password = getpass("Enter your password: ")

#Function to kick off site scan. Modify as needed. 
def runscan():
    """Performs a scan based off the information provided."""
    global SCANID
    siteid = input("Enter the site ID: ")
    urllib3.disable_warnings()
    url = f"https://{host}:3780/api/3/sites/{siteid}/scans"
    headers = {
        "Content-Type": "application/json",
    }
    payload = json.dumps(
        {
            "engineId": "",
            "hosts": [],
            "name": "APIscan",
            "templateId": "full-audit-without-web-spider",
        }
    )
    response = requests.post(
        url,
        auth=HTTPBasicAuth(user, password),
        headers=headers,
        data=payload,
        verify=False,
    ).json()
    SCANID = response["id"]
    return SCANID

#Function to Check the status of the scan that was kicked off
def checkrunning():
    """Checksthe scan status of the scan created"""
    urllib3.disable_warnings()
    id = SCANID
    url = f"https://{host}:3780/api/3/scans/{id}"
    payload = json.dumps({"status": ""})
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.get(
        url,
        auth=HTTPBasicAuth(user, password),
        headers=headers,
        data=payload,
        verify=False,
    ).json()
    return response["status"]


# Main
sid = runscan()
status = checkrunning()
print(f"The scan id is {sid} and its current status is {status}.")
