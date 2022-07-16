import requests
import json
import time
import os
import random

status = ["Website: am1r.tech", "IG: @am1r__8", "JUST A BORED PROGRAMMER", "I call my self a developer but I can't develop a fucking relationship", "are you a rusher, or are you a dragger or are you gonna be ON MY FUCKING TIME?", "I gotta tell u it was perfect, perfect everything down to the last minute details", "The most harmful words in the English language are GOOD JOB"]
token = os.environ.get('token')
emojies = ["📢", "🎮", "👨‍💻", "💻", "💬", "✨", ""]
photos = []
emo = ""
delay = 10
class main:
    def __init__(self, token, status):
        self.token = token
        self.status = status
        self.emojies = emojies
        self.emo = emo
        try:
            while True:
                for i in range(len(self.status)):
                    self.emo = self.emojies[i]
                    self.set_status(self.status[i])
                    time.sleep(delay)
        except KeyboardInterrupt:
            print("Stopped auto status!")
            exit()
    def set_status(self, status):
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":status,"emoji_name":self.emo}}))

if __name__ == "__main__":
    if requests.patch("https://discord.com/api/v9/users/@me", headers={"authorization": token,"content-type": "application/json"}).status_code == 400:
        main(token, status)
    else:
        print("Failed to connect to discord, please check your token")
        exit()