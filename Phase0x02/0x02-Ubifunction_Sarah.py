'''
This code demonstrates a simple webhook endpoint that receives a POST request from dialogflow
and fulfills the response to user at some integrations:

    Web Demo:
    https://bot.dialogflow.com/3b6b0c55-7d58-4273-be17-12256f0dbc6c

'''

import requests

def create_request(token, device, variable):
    '''
    Function to create a request to the server
    '''

    endpoint = "industrial.api.ubidots.com"
    url = "http://{}/api/v1.6/devices/{}/{}/lv".format(endpoint, device, variable)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    req = requests.get(url=url, headers=headers)

    return req.text
    
def main(args):
    '''
    Main function - runs every time the function is executed.
    "args" is a dictionary containing both the URL params and the HTTP body (for POST requests).
    '''

    result = args.get('queryResult')
    parameters = result.get('parameters')
    device = parameters.get('Device')
    variable = parameters.get('Variables')
    token = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"

    fulfillment = create_request(token, device, variable)

    speech = "The last value of {} from {} is {}".format(variable, device, fulfillment)

    return {"speech": speech,"fulfillmentText": speech,"source": "SarahDots"}
