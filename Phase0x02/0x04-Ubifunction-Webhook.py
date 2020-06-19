'''
This code demonstrates a simple webhook endpoint that receives a POST request from dialogflow
and fulfills the response to user at some integrations:

    Web Demo:
    https://bot.dialogflow.com/3b6b0c55-7d58-4273-be17-12256f0dbc6c

'''
import requests
import json


def default():
    return "Invalid Action"


def get_last_value(result, token):
    parameters = result.get('parameters')
    device = parameters.get('Device')
    variable = parameters.get('Variables')

    endpoint = "industrial.api.ubidots.com"
    url = "http://{}/api/v1.6/devices/{}/{}/lv".format(endpoint, device, variable)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}
    req = requests.get(url=url, headers=headers)

    return "The last value of {} from {} is {}".format(variable, device, req.text)


def get_all_devices(token):
    endpoint = "industrial.api.ubidots.com"
    url = "https://{}/api/v2.0/devices/".format(endpoint)

    headers = {"X-Auth-Token": token}
    req = requests.get(url=url, headers=headers)
    devices = []

    req_dict = json.loads(req.text)
    n_devices = req_dict.get('count')
    devices_list = req_dict.get('results')

    for device in range(0, n_devices, 1):
        devices.append(devices_list[device].get('label'))

    return "Here is the list of your devices with their labels: " + ", ".join(devices)


def get_all_variables(result, token):
    endpoint = "industrial.api.ubidots.com"
    url = "https://{}/api/v2.0/variables/".format(endpoint)
    parameters = result.get('parameters')
    device = parameters.get('device')

    headers = {"X-Auth-Token": token}
    req = requests.get(url=url, headers=headers)
    device_varables = []

    req_dict = json.loads(req.text)
    variables_list = req_dict.get('results')

    for variable in variables_list:
        device_info = variable.get('device')
        if device == device_info.get('label'):
            device_varables.append(variable.get('label'))

    return "Here is the list of your variables from {} with their labels: ".format(device) + ", ".join(device_varables)


def create_request(action, result, token):
    '''
    Function to create a request to the server
    '''
    sw = {'RequestLvUbidots': get_last_value(result, token),
          'RequestAllDevicesUbidots': get_all_devices(token),
          'RequestAllVarUbidots': get_all_variables(result, token)}
    return sw.get(action, default())


def main(args):
    '''
    Main function - runs every time the function is executed.
    "args" is a dictionary containing both the URL params and the HTTP body (for POST requests).
    '''

    result = args.get('queryResult')
    action = result.get('action')
    setup(args)
    token = args.get('token')

    speech = create_request(action, result, token)

    return {"speech": speech, "fulfillmentText": speech, "source": "SarahDots"}


def setup(args):
    '''
        Function to setting up the token
    '''

    args['token'] = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8"

    return