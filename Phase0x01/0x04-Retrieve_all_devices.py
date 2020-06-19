#!/usr/bin/env python
"""
    Second Example for retrieving all devices
"""

import requests
import time
import json

ENDPOINT = "industrial.api.ubidots.com"
TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"


def get_all_devices(url=ENDPOINT, token=TOKEN):


    try:
        url = "https://{}/api/v2.0/devices/".format(url)
        devices = []
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
        n_devices = req_dict.get('count')
        devices_list = req_dict.get('results')
        for device in range(0, n_devices, 1):
            devices.append(devices_list[device].get('label'))
        print("Here is the list of your devices with their labels: " + ", ".join(devices))


    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

if __name__ == "__main__":
    get_all_devices()
