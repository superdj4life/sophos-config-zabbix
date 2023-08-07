#!/usr/bin/env python3

"""
version = 0.1apha
tested python version = 3.9
tested Sophos = 9.6
tested Sophos API = 1.3.6
tested Zabbix Server = 4.0.2
"""

import sys
import requests
import logging
import urllib3
from requests.auth import HTTPBasicAuth

### mute SSL errors ###
urllib3.disable_warnings()

### define static variables ###
json_start = "{\"data\":["
json_end = "]}"
verification = False  # To verify the SSL certificate or not to verify the SSL certificate. Accepted: True/False

### define passed arguments ###
host = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
method = sys.argv[5]
call_type = sys.argv[6]

### Sophos UTM API related parameters ###
sophos_headers = {
    "Accept": "application/json"
}

### testing the API method with automatic discovery ###
def universal_method(host, port, method, call_type, username, password):
    call = requests.get(
        f"https://{host}:{port}/api/objects/{method}/{call_type}/",
        headers=sophos_headers,
        auth=HTTPBasicAuth(username, password),
        verify=verification
    )
    json_formatted_output = call.json()
    print(json_start)
    for num in range(0, len(json_formatted_output)):
        object_items_count = len(json_formatted_output[num]) - 1
        print("{")
        for key, value in json_formatted_output[num].items():
            if object_items_count >= 1:
                object_items_count -= 1
                print(f"\"{{#{key.upper()}}}\":\"{value}\",")
            elif object_items_count == 0:
                print(f"\"{{#{key.upper()}}}\":\"{value}\"")
        if num < len(json_formatted_output) - 1:
            print("},")
        elif num == len(json_formatted_output) - 1:
            print("}")
    print(json_end)

universal_method(host, port, method, call_type, username, password)
