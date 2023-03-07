#!/usr/bin/env python3
#
#  Description: Script that uses the Nexpose APIv3 to create a Dynamic Asset Group based off the criteria provided.

import json
from getpass import getpass

import urllib3
import requests
from requests.auth import HTTPBasicAuth

# Prompts to collect nexpose console and login information
host = input("Enter the server name (host) for InsightVM: ")
user = input("Enter your username: ")
password = getpass("Enter your password: ")

#Function creating the asset group and printing results
def create_ag():
    """creates a dynamic asset group based off criteria and prints out the id with a url."""
    urllib3.disable_warnings()
    url = f"https://{host}:3780/api/3/asset_groups"
    headers = {
        "Content-Type": "application/json",
    }
    payload = json.dumps(
        {
            "description": "Assets with unacceptable high risk required immediate remediation.",
            "name": "High Risk Assets",
            "searchCriteria": {
                "filters": [
                    {
                        "field": "risk-score",
                        "lower": "",
                        "operator": "is-greater-than",
                        "upper": "",
                        "value": 25000,
                        "values": ["string"],
                    }
                ],
                "match": "all",
            },
            "type": "dynamic",
            "vulnerabilities": {},
        }
    )
    response = requests.post(
        url,
        auth=HTTPBasicAuth(user, password),
        headers=headers,
        data=payload,
        verify=False,
    ).json()
    agid = response["id"]
    print(
        f"Asset Group {agid} created and can be found at https://{host}:3780/group.jsp?groupid={agid}"
    )
    return


# Main
create_ag()
