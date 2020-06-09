var request = require('request-promise');

// Main function - runs every time the function is executed.
// "args" is a dictionary containing both the URL params and the HTTP body (for POST requests).
async function main(args) {

  // Grab the token and device label from URL parameters, then erase them from the args dictionary
  const ubidots_token = "BBFF-o9Wgd3hZokBMNd7d4vyzH9ZfLa5qj8";
  const device_label = "weather-station/temperature";

  // Send the payload to Ubidots
  var response = await ubidots_request(ubidots_token, device_label);

  console.log(response);

  return response;
}

async function ubidots_request(token, label) {
  const options = {
    method: 'GET',
    url: 'https://industrial.api.ubidots.com/api/v1.6/devices/' + label,
    body: body,
    json: true,
    headers: {
      'Content-Type': 'application/json',
      'X-Auth-Token': token
    }
  };
  return request.get(options);
}