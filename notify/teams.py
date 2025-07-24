import json
import os
<<<<<<< HEAD
import requests

=======

import requests


>>>>>>> 02185a2 (updated)
class TeamsNotifier:
    @staticmethod
    def env_checked_out(env_name, username, time, comment):
        try:
            with open('teams_msg.json', 'r') as file:
                data = json.load(file)

            data["attachments"][0]["content"]["body"][1]["text"] = (
                f"Environment **{env_name.upper()}** is occupied by **{username}** "
                f"for **{time} hours**.\n\n**Comment**: {comment}"
            )

            TeamsNotifier._post_to_teams(data)

        except Exception as e:
            print(f"[TeamsNotifier][Checkout] Failed: {e}")

    @staticmethod
    def env_released(env_name):
        try:
            with open('teams_msg.json', 'r') as file:
                data = json.load(file)

            data["attachments"][0]["content"]["body"][1]["text"] = (
                f"Environment **{env_name.upper()}** is available now"
            )

            TeamsNotifier._post_to_teams(data)

        except Exception as e:
            print(f"[TeamsNotifier][Release] Failed: {e}")

    @staticmethod
    def _post_to_teams(data):
        api_url = os.getenv("TEAMS_WEBHOOK")
        headers = {"Content-Type": "application/json"}
        if api_url:
            requests.post(api_url, json=data, headers=headers)
        else:
            print("[TeamsNotifier] TEAMS_WEBHOOK not configured")