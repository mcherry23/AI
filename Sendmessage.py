import requests

ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"

def send_message(user_id, text):
    url = "https://graph.facebook.com/v19.0/me/messages"

    payload = {
        "recipient": {"id": user_id},
        "message": {"text": text},
        "access_token": ACCESS_TOKEN
    }

    requests.post(url, json=payload)
