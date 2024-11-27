from PySide6.QtWidgets import *
from alcohol_whale_ui import Ui_Form

from time import sleep
#from picamera import PiCamera
import requests
import json
from pprint import pprint
import os
import subprocess


class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    # page 연결 함수
    cur_page_num = 0

    def nextPage(self):
        global cur_page_num
        #현재 페이지 index 출력
        cur_page_num = self.stackedWidget.currentIndex();
        print(cur_page_num)
        self.stackedWidget.setCurrentIndex(cur_page_num+1);

    def pastPage(self):
        global cur_page_num
        cur_page_num = self.stackedWidget.currentIndex();
        print(cur_page_num)
        self.stackedWidget.setCurrentIndex(cur_page_num - 1);

    def move_home(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def takeApicture(self):
        cam = PiCamera()
        cam.start_preview()
        for i in range(5):
            print(i)
            sleep(1)
        cam.capture('./yourFace.jpg')
        cam.stop_preview()

    def Capture_display():
        os.system("rm ./capture.jpg")  # 같은이름으로 덮어쓰려고
        os.system("scrot ./capture.jpg")

    # 파일이 현재 폴더위치에 저장!

    def send_kakao(self):
        pass

    def move_survey(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def move_sentiment(self):
        self.stackedWidget.setCurrentWidget(self.page_15)

    def send_min_range(self):
        print("send min")

    def send_max_range(self):
        print("send max")

    def Face_recog(self):
        client_id = ""
        client_secret = ""
        target = 'yourFace.jpg'

        url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
        files = {'image': open(target, 'rb')}
        headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret}
        response = requests.post(url, files=files, headers=headers)
        response_code = response.status_code

        my_json = json.loads(response.text)
        if response_code == 200:
            pprint(my_json, indent=2)
        else:
            print("Error Code:" + response_code)


    def ImgName(self):
        kiosk_id = "SSAFY4"
        output = subprocess.run("date", stdout=subprocess.PIPE, text=True)
        output = output.stdout
        name = kiosk_id + "_" + output[4:6] + "_" + output[16:18] + output[19:21] + output[22:24] + ".jpg"
        # print(name)
        return name

    # 리턴값 사용하면 됩니다
    # ex 8월10일16시01분30초 의경우
    # SSAFY4_10_040130.jpg 로 저장!

    def connect_s3(self):
        try:
            Bucket = boto3.client(
                service_name="s3",
                region_name="ap-northeast-2",
                aws_access_key_id="",
                aws_secret_access_key="",
            )

        except Exception as e:
            print(e)
        else:
            print("connected")
            return Bucket

    def Upload_s3(self):
        global upload_name

        myBucket = self.connect_s3()
        bucket_name = "alcoholwhale"

        try:
            # upload img here
            upload_name = self.ImgName()  # 이름 설정하는 함수 실행
            myBucket.upload_file("./capture.jpg", bucket_name, upload_name)
        except Exception as e:
            print(e)
        else:
            print("uploaded")

    def QR_generator(self):
        global upload_name
        my_url = "https://alcoholwhale.s3.ap-northeast-2.amazonaws.com/" + upload_name

        img_url = qrcode.make(my_url)
        img_url.save("./qr.png")
        # img_url.show()

app = QApplication()
win = MyApp()

win.show()
app.exec()