import requests
import json
import time
import os
import random

status = ["EMORY TATE"]
token = os.environ.get('token')
emojies = [""]
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