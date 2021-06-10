from flask import Flask
app = Flask(__name__)

@app.route("/status")
def status():
    return {"status": "Ok - healthy"}

@app.route("/metrics")
def metrics():
    return {"data": {"UserCount": 140, "UserCountActive": 23 }}

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
