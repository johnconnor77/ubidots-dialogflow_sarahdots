#!/usr/bin/env python
"""
    First Example for retrieving data of device Weather Station
"""

import requests
import time


ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "river-sensor"
VARIABLE_LABEL = "flow"
TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"


def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable=VARIABLE_LABEL,
            token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}/{}/lv".format(url, device, variable)

        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            print("[INFO] Retrieving data, attempt number: {}".format(attempts))
            req = requests.get(url=url, headers=headers)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)

        """print("[INFO] Results:")
        print(req.text)"""
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))


if __name__ == "__main__":
    get_var()
