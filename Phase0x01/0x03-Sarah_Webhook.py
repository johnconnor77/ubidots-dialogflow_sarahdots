#!/usr/bin/env python

#  ███████╗ █████╗ ██████╗  █████╗ ██╗  ██╗
#  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║  ██║
#  ███████╗███████║██████╔╝███████║███████║
#  ╚════██║██╔══██║██╔══██╗██╔══██║██╔══██║
#  ███████║██║  ██║██║  ██║██║  ██║██║  ██║
#  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝


# !/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
import requests

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    """
            Function for parsing info that comes from dialogflow
    """
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(req):
    """
        Function that realize the query based on device and variable labels
    """
    
    result = req.get('queryResult')
    parameters = result.get('parameters')
    device = parameters.get('Device')
    variable = parameters.get('Variables')

    """DEVICE_STR = str(req.query_result.parameters['Device'].values[0])
    DEVICE_LABEL = DEVICE_STR.replace('"', '').split()[1]
    VARIABLE_STR = str(req.query_result.parameters['Variables'].values[0])
    VARIABLE_LABEL = VARIABLE_STR.replace('"', '').split()[1]"""

    endpoint = "industrial.api.ubidots.com"

    token = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"

    url = "http://{}/api/v1.6/devices/{}/{}/lv".format(endpoint, device, variable)

    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    req_dots = requests.get(url=url, headers=headers)

    speech = "The last value of {} from {} is {}".format(variable, device,req_dots.text)

    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "fulfillmentText": speech,
        "source": "SarahDots"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % (port))

    app.run(debug=True, port=port, host='0.0.0.0')
