import urllib.request
import json
import os
import ssl
from flask import Flask, render_template, request

app = Flask(__name__)


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_azure', methods=['POST'])
def predict_azure():
    data = {
        "Inputs": {
            "data": [
                {
                    "day": int(request.form['day']),
                    "mnth": int(request.form['month']),
                    "year": int(request.form['year']),
                    "season": int(request.form['season']),
                    "holiday": int(request.form['holiday']),
                    "weekday": int(request.form['weekday']),
                    "workingday": int(request.form['workingday']),
                    "weathersit": int(request.form['weathersit']),
                    "temp": float(request.form['temp']),
                    "atemp": float(request.form['atemp']),
                    "hum": float(request.form['hum']),
                    "windspeed": float(request.form['windspeed'])
                }
            ]
        },
        "GlobalParameters": 0.0
    }

    body = str.encode(json.dumps(data))
    print("Body: " + body.decode())

    url = os.environ.get('AZURE_ENDPOINT_URL')
    api_key = os.environ.get('AZURE_API_KEY')
    
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")

    headers = {'Content-Type': 'application/json',
               'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        prediction = json.loads(result)['Results'][0]
        return render_template('index.html', prediction=prediction)

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))


if __name__ == '__main__':
    app.run(debug=True)
