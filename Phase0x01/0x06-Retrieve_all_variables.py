#!/usr/bin/env python
"""
    Third Example for retrieving data of variables from a device
"""

import requests
import time
import json


ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "river-sensor"
TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"


def get_all_var(url=ENDPOINT, device=DEVICE_LABEL,
            token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}/".format(url, device)

        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Retrieving data, attempt number: {}".format(attempts))
            req = requests.get(url=url, headers=headers)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        print("[INFO] Results:")
        print(req.text)

        req_dict = json.loads(req.text)
        variables_url = req_dict.get('url') +"/variables"

        req_variables = requests.get(variables_url, headers=headers)

        print(req_variables.text)


        print(variables_url)

    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

    return req.text


if __name__ == "__main__":
    result = get_all_var()