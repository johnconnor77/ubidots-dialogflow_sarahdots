#!/usr/bin/env python

#  ███████╗ █████╗ ██████╗  █████╗ ██╗  ██╗
#  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║  ██║
#  ███████╗███████║██████╔╝███████║███████║
#  ╚════██║██╔══██║██╔══██╗██╔══██║██╔══██║
#  ███████║██║  ██║██║  ██║██║  ██║██║  ██║
#  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
#
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests
import time
import json


ENDPOINT = ""
DEVICE_LABEL = ""
VARIABLE_LABEL = ""
TOKEN = ""


def get_var(url=ENDPOINT, device=DEVICE_LABEL, variable=VARIABLE_LABEL,
            token=TOKEN):
    try:
        url = "http://{}/api/v1.6/devices/{}/{}/lv".format(url, device, variable)

        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
            """print("[INFO] Retrieving data, attempt number: {}".format(attempts))"""
            req = requests.get(url=url, headers=headers)
            status_code = req.status_code
            time.sleep(1)

        """print("[INFO] Results:")
        print(req.text)"""
    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

    return req.text


if __name__ == "__main__":

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'sarahdots-gtmiej-c64dd83054be.json'

    DIALOGFLOW_PROJECT_ID = 'sarahdots-gtmiej'
    DIALOGFLOW_LANGUAGE_CODE = 'en'
    SESSION_ID = 'me'
    ENDPOINT = "industrial.api.ubidots.com"
    TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"
    OUT = ""

    text_to_be_analyzed = "Can you tell me the last value of flow from River sensor?"

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    #response2 = response.get('queryResult')
    print(response)
    print("Query text:", response.query_result.query_text)
    DEVICE_STR = str(response.query_result.parameters['Device'].values[0])
    DEVICE_LABEL = DEVICE_STR.replace('"', '').split()[1]
    VARIABLE_STR = str(response.query_result.parameters['Variables'].values[0])
    VARIABLE_LABEL = VARIABLE_STR.replace('"', '').split()[1]

    OUT = get_var(ENDPOINT, DEVICE_LABEL, VARIABLE_LABEL, TOKEN)

    print("Fulfillment text:", response.query_result.fulfillment_text + " " + OUT)