#import os
import requests
import json
from time import time
from pprint import pprint
from picamera import PiCamera
from time import sleep

#Initial Setting, Variavles
cam = PiCamera()
client_id=""
client_secret=""
target='capture.jpg'

#Camera, capture
print("START NOW")
sleep(1)

cam.start_preview()
sleep(10)
cam.capture('./capture.jpg')
cam.stop_preview()

#analyze pic
now = time()
url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
files = {'image': open(target, 'rb')}
headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret}
response = requests.post(url, files=files, headers=headers)
response_code = response.status_code

print(f"실행 시간 : {round(time() - now, 3)} 초")

my_json = json.loads(response.text)
if response_code == 200:
    pprint(my_json, indent=2)
else:
    print("Error Code:" + response_code)
