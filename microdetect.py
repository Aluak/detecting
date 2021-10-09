import requests
import json
import pandas as pd
from datetime import datetime
from time import sleep

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRiuTLwcN5WULnOKFp9oGqKzlllwUMLQp2S2nG0mufpJVuForfKCxZ7O2hLNJCLTtN6PMJouof_LJnz/pubhtml")
Micro_ID = '0Af201'

MIC_ID = '0AF201' # 000001 - FFFFFF  hexadecimal

now = datetime.now() # real time 

interval = 2 # interval of cameral detecting

txt = {
    "mic_id": MIC_ID,
    "mic_danger": "False",
    "mic_time": '{}.{}.{} {}:{}'.format(now.year, now.month, now.day, now.hour, now.minute)
}                       # class of detecting year, month, day, minute



def start(Cam_ID):
    r = requests.get('http://127.0.0.1:8000/api/v1/all/').text
    list1 = json.loads(r)
    for i in list1:
        if i['mic_ic'] == Cam_ID:
            return i['id']
    requests.post('http://127.0.0.1:8000/api/v1/create/', txt)
    return start(Cam_ID) # request to get information from camera

class Cam():
    def __init__(self, id):
        self.id = start(id)

    def send_rq(self):
        data = {
            "mic_id": MIC_ID,
            "mic_danger": "True",
            "mic_time": '{}.{}.{} {}:{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        }
        requests.put('http://127.0.0.1:8000/api/v1/deteil/{}'.format(self.id), data)    

    def get_sound(self):
        return (input("sound type: "))

    def analyze(df):
        if df[df["name"] == "axe" ] or df[df["name"] == "chainsaw"]:
            return True
        else:
            return False               # checking type of sound 

def main(MIC_ID):
    micro = Cam(MIC_ID)
    sound_1 = temperature_2 = micro.get_sound()
    while True:
        if micro.analyze(sound_1, sound_2):
            micro.send_rq()
        sleep(interval)
        sound_1, sound_2 = temperature_2, micro.get_sound()
        


if __name__ == '__main__':
    main(MIC_ID)
