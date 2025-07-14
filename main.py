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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
