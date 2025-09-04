import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/wait", methods=["GET"])
def wait():
    time.sleep(4)  # wait exactly 4 seconds
    return jsonify({"status": "timeout", "message": "4 seconds passed"})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)