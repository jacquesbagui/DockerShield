import requests
from src.core.notifier import Notifier

class SlackNotifier(Notifier):
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def notify(self, message):
        payload = {
            "text": message
        }
        response = requests.post(self.webhook_url, json=payload)
        if response.status_code != 200:
            raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")