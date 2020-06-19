#!/usr/bin/env python
"""
    Third Example for retrieving data of variables from a device
"""

import requests
import time
import json

ENDPOINT = "industrial.api.ubidots.com"
TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"
DEVICE = "river-flood"


def get_all_var(url=ENDPOINT, token=TOKEN, device=DEVICE):


    try:
        url = "https://{}/api/v2.0/variables/".format(url)
        device_varables = []
        headers = {"X-Auth-Token": token}

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
        variables_list = req_dict.get('results')

        for variable in variables_list:
            device_info = variable.get('device')
            if device == device_info.get('label'):
                device_varables.append(variable.get('label'))

        print("Here is the list of your variables from {} with their labels: ".format(device) + ", ".join(device_varables))



    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

if __name__ == "__main__":
    get_all_var()