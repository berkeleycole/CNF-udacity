from flask import Flask
from flask import json
import logging

app = Flask(__name__)

# STATUS ENDPOINT
@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/status endpoint success')

    return response

# METRICS ENDPOINT
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/metrics endpoint success')

    return response

# ROOT
@app.route("/")
def hello():
    app.logger.info('root endpoint success')
    return "Hello World!"

if __name__ == "__main__":
    # Collect DEBUG level logs in app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
