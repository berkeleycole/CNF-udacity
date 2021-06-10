from flask import Flask
import logging

app = Flask(__name__)
root_logger= logging.getLogger()

# Collect DEBUG level logs in app.log file
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

# STATUS ENDPOINT
@app.route("/status")
def status():
    logging.debug('status endpoint was reached')
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

# METRICS ENDPOINT
@app.route("/metrics")
def metrics():
    logging.debug('metrics endpoint was reached')
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

# ROOT
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
