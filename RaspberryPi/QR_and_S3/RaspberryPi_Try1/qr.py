import qrcode
import boto3
from time import sleep
from picamera import PiCamera
from naming import ImgName

bucket_name="alcoholwhale"
cam=PiCamera()


def connect_s3():
    try:
        myBucket=boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="액세스키 입력",
            aws_secret_access_key="시크릿키 입력",
        )

    except Exception:
        print(Exception)
    else:
        print("connected")
        return myBucket
myBucket=connect_s3()



try:
    #take picture here
    cam.start_preview()
    for i in range(5):
        print(i)
        sleep(1)
    cam.capture('./capture.jpg')
    cam.stop_preview()

    #upload img here
    upload_name=ImgName()
    myBucket.upload_file("./capture.jpg",bucket_name,upload_name)

except Exception as e:
    print(e)
else:
    print("uploaded")
    my_url="https://alcoholwhale.s3.ap-northeast-2.amazonaws.com/"+upload_name
    img_url=qrcode.make(my_url)
    img_url.save("./qr.png")
    img_url.show()

##########



