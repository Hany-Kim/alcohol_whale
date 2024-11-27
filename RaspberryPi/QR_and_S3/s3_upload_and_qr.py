import qrcode
import boto3


bucket_name="alcoholwhale"
def connect_s3():
    try:
        myBucket=boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="액세스 키",
            aws_secret_access_key="시크릿 키",
        )
    except Exception:
        print(Exception)
    else:
        print("connected")
        return myBucket
myBucket=connect_s3()

try:
    #업로드할 이름 설정 필요함
    upload_name="upload_ex.jpg"
    myBucket.upload_file("C:/Users/SSAFY/Desktop/example.jpg",bucket_name,upload_name)
except Exception as e:
    print(e)
else:
    print("uploaded")
    my_url="https://alcoholwhale.s3.ap-northeast-2.amazonaws.com/"+upload_name
    img_url=qrcode.make(my_url)
    img_url.save("C:/Users/SSAFY/PycharmProjects/QR/qr.png")
    img_url.show()

##########



