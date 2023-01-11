#! /usr/bin/python3

import requests
import json
from tgtg import TgtgClient
import os


CONFIG_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/config.json"


def send_notification(subject, article_name):
    s = requests.Session()
    headers = {
        "Title": "Panier disponible !",
        "Priority": "urgent",
        "Tags": "tada"
    }
    data = f"Un nouveau panier chez {article_name} est disponible".encode("utf-8")
    s.post(f"https://ntfy.sh/{subject}", headers=headers, data=data)

# Read config file to get all last available articles (avoid spam)
# Recover account config
subject, last_available_articles, access_token, refresh_token, user_id = None, None, None, None, None
with open(CONFIG_FILE, "r") as f:
    config = json.load(f)
    subject = config["subject"]
    access_token = config["access_token"]
    refresh_token = config["refresh_token"]
    user_id = config["user_id"]
    last_available_articles = config["available"]


# Create tgtg client object
client = TgtgClient(access_token=access_token, refresh_token=refresh_token, user_id=user_id)

# Query favourites
items = client.get_items()

# For each item, check if there is at least one available, and if it was not already available previously
# If a previously availabe article is not availabe anymore, remove from availibility list
for item in items:
    nb_items = int(item["items_available"])
    item_name = item["display_name"]
    if nb_items > 0 and item_name not in last_available_articles:
        last_available_articles.append(item_name)
        send_notification(subject, item_name)
    elif nb_items == 0 and item_name in last_available_articles:
        last_available_articles.remove(item_name)

# Update config file
config["available"] = last_available_articles
with open(CONFIG_FILE, "w") as f:
    json.dump(config, f)