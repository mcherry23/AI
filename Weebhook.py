from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    try:
        message = data["entry"][0]["messaging"][0]["message"]["text"]
        sender_id = data["entry"][0]["messaging"][0]["sender"]["id"]

        reply = generate_reply(message)
        send_message(sender_id, reply)

    except:
        pass

    return "ok"
