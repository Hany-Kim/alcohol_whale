import os
import subprocess

def ImgName():
    output = subprocess.run("date", stdout=subprocess.PIPE,text=True)
    output=output.stdout
    name=output[4:6]+"_"+output[16:18]+output[19:21]+output[22:24]+".jpg"
    print(name)
    return name
