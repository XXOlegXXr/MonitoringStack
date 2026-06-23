from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    status = data.get("status", "unknown").upper()

    for alert in data.get("alerts", []):
        name = alert["labels"].get("alertname", "Alert")
        summary = alert["annotations"].get("summary", "")
        description = alert["annotations"].get("description", "")
        instance = alert["labels"].get("instance", "")

        text = f"[{status}] {name}\n{summary}\n{description}\nInstance: {instance}"

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text},
            timeout=10
        )

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
