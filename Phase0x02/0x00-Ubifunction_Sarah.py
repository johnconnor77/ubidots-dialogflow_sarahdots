'''
This code demonstrates a session inside a dialogflow bot for parsing intents
    Web Demo:
    https://bot.dialogflow.com/3b6b0c55-7d58-4273-be17-12256f0dbc6c
'''

import requests
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
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

    except Exception as e:
        print("[ERROR] Error posting, details: {}".format(e))

    return req.text



def ubifunc(args):
    '''
    Main function - runs every time the function is executed.
    "args" is a dictionary containing both the URL params and the HTTP body (for POST requests).
    '''
    token = args.get('token', None)
    query = args.get('query', None)

    if token is None or query is None:
        print("[ERROR] Please send your Ubidots Token and query to update in your args")
        return {"status": "error"}

    del args['token']
    del args['query']

    SARAH_CREDENTIALS = {
        "type": "service_account",
        "project_id": "sarahdots-gtmiej",
        "private_key_id": "c64dd83054be36011f7900872da1e4f9759d04a7",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCke22x/9OmMDtL\n04PxjP3g6x/HPJsO6QL9EK7BgpuLku1QLeVjTWOZHm9xbRNcA+9WZFpl75UIoqgQ\n/yKkrcXSR4EbxtwAfDNu/gmyK4R0yG83gwzyUBJulVInQVGB/PYso5YCDcR9ijFg\nyuOC7rhgdgJPuHMJVIqVLe8fpAwWoquHt9wjzcDCxHTLD6Y54533nwyxVgL1eIM7\nnIK3s7HK3J+feuTxQZ/WcHsCp1qdZuLXSl8SwJnlaJQbbMaGW8Tw9fQTysW7tRSP\nav2nT+36OIY30bBk3Qoag/f+8RVZU+1G+keiTy/KGmCQQ/Zge9Uz/R+RgSo/ihGq\nBhgNNShXAgMBAAECggEAGHRmIPlaw+eBjBVfas9IwyM3dH1dG8Xmv65hH9Hl2MYY\nX3vmEjIO3/9HmB3HVj5wMVrhRSzuQ7w/RaumlcUPrOMcXdSz9U8srHtmVfr6Cgzv\nhYQyrWeHSLFjEgVi83MjPLbOVkbVaHQz7DgDbyjuo8otL3d1LwrGl0XJkDLpPdy7\njyrZD19Wir0byPcbGKaNAYw1d6EwAAw6XQc6gXq167XmJ35ymvpzh2WdEDPnAVik\nifRKRUhGs/1zq7p2DbcNIBLvVPfMETFyz6sjivSmVuPfF/BCHZPdw8c8Pd7X+pXs\nRD0KKw6TRCJvG6BjUZ8Ir26lICLyYo2khXAseqLf7QKBgQDYLIHdNRUunD9yCmKg\nnMjsTH5I19JokLB+DWjjcJ+/yNOBMEqlO63jjpmrzwjetIvc9kubd/SYGlS32c33\ny/s2ylRDnAaIh/14z8PtsRmmOmCYhqre9EtsCYD8Gfk6SDv1yfGCOPccm6bEWdm0\nN4h5myWI1oNrQO7VCWek1tjBfQKBgQDCyPbtA0zAxjmX6VPWJivR5gSIxk3uwkow\nGpc+hZJF53g1jHQ1z4iJ4Tr9To7/1mLYKmgQmap6h0IpkHmxoENucv84Kov3OD16\nZXaFkguhoxqffI+xumWBOl6pxVnJu5lxsXMdGX1SU9mySgBw3UnFPwPGLS9cs+lU\n2Vm1dvu5YwKBgQChAaVHyL2aFa37lliXH69WsDJutrB0SS/q8rnojH2vLji5w+oU\n3zpIfnFeUbldhkOVs6vkg5edoh7vQD30De1xhYj1QkRrdD4JuVVIt9tOv7QqZkLm\nBDYYpYt4OTAzhJGEI4DJaPxERnoTTIilfaccS73NCVigjaBU88hKMesHUQKBgQCY\neUG5VFzvhfuta4sh1i11GA4ylrCIlnQGZbpAycQvjjquCC0rtjHWZIWNpcIQiFxF\nhCSD4hXt5hUnfh2UqrQ+MCySZdO8iLyvI998PU93jrqXX6UH5bXxS6SwVnirjntV\n4ScP/1T3bgW6J21i7AYELgihR9uMQJUEw0MS5nmzqwKBgQDHE2onRIXD4aPQWRPC\nGe75onQNMdYRUTerEi2vA9c/Dsj4DwBTJVpeQU03BNM4rlmLwAknE+DvocGlzeKc\n/RU++ZJy46RACe8+Vf9iPYVPVs4cGjLNiCwjRmUO9Tsvv29l6Vc5dPkl3SVegedo\nEvhJxxdmt7pAeeWQc43g73hs8w==\n-----END PRIVATE KEY-----\n",
        "client_email": "dialogflow-integrations@sarahdots-gtmiej.iam.gserviceaccount.com",
        "client_id": "109751044216416218514",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/dialogflow-integrations%40sarahdots-gtmiej.iam.gserviceaccount.com"
    }

    with open('credentials.json', 'w') as f:
        json.dump(SARAH_CREDENTIALS, f)

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

    DIALOGFLOW_PROJECT_ID = 'sarahdots-gtmiej'
    DIALOGFLOW_LANGUAGE_CODE = 'en'
    SESSION_ID = 'me'
    ENDPOINT = "industrial.api.ubidots.com"
    TOKEN = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"
    OUT = ""

    text_to_be_analyzed = query

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print(response)
    print("Query text:", response.query_result.query_text)

    DEVICE_LABEL = response.query_result.parameters['Device']
    VARIABLE_LABEL = response.query_result.parameters['Variables']

    OUT = get_var(ENDPOINT, DEVICE_LABEL, VARIABLE_LABEL, TOKEN)

    result = response.query_result.fulfillment_text + " " + OUT

    return {"status": "Ok", "result": result}


if __name__ == "__main__":

    query_ans = ubifunc(args = {"query": "What is the last value of flow from river-sensor?", "token": "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"})
