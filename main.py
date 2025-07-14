from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_request():
    """Handles webhook requests from Dialogflow CX."""
    req = request.get_json(force=True)
    tag = req.get("fulfillmentInfo", {}).get("tag")
    if tag == "Default Welcome Intent":
        text = "Hello from a webhook!"
    else:
        text = f"Webhook received: {tag}"

    fulfillment_response = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [text]
                    }
                }
            ]
        }
    }
    return jsonify(fulfillment_response)

import requests

@app.route("/sr/<int:sr_number>", methods=["GET"])
def get_sr_details(sr_number):
    """Fetches SR details from the Sanmina API."""
    url = f"https://itdev.sanmina.com/hdapi/ittest/SR/Details/{sr_number}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
