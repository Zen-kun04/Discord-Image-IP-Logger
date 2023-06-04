import random
import requests
from dotenv import load_dotenv
from os import environ

load_dotenv()
user_token = environ.get("TOKEN")
testing_id = environ.get("SOME-ID")

image_url = input("Image url: ").strip()

# Check if there's a valid url
if image_url == "" or (not image_url.startswith('http://') and not image_url.startswith('https://')):
    exit()

nonce = random.randint(0, 2**64) # Generate a nonce

headers = {
    'authorization': user_token
}

# Discord request for sending a message
r = requests.post(f"https://discord.com/api/v9/channels/{testing_id}/messages", {
    "content": image_url,
    "nonce": nonce,
    "tts": False,
    "flags": 0
},
headers=headers)

json = r.json()

if json["embeds"]:
    print(json["embeds"][0]["thumbnail"]["proxy_url"]) # Here's the magic link ;)