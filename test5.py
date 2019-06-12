import os
import urllib
from urllib import request


title = "妩媚女神妲己_Toxic 纱薄轻遮妙曼影"
num1 = "30039"
num3 = "009"
img = "https://t1.onvshen.com:85/gallery/22359/" + num1 + "/" + num3 + ".jpg"

require = urllib.request.Request(img)
reponse = urllib.request.urlopen(require)

photo = reponse.read()
path = "E:\妲己_Toxic\\" + num1 + title + "\\"
y = os.path.exists(path)
if y != 1:
    os.makedirs(path)

with open(path + num3 + ".jpg", 'wb') as f:
    print('开始下载图片')
    f.write(photo)
    f.close()