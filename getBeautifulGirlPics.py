# coding=UTF-8
# 下载美女图片
# 图片源：https://www.nvshens.com/girl/22359/album/

import os
import re
import time
import urllib
from reprlib import repr

from bs4 import BeautifulSoup
import requests
from urllib import request, error
import logging

# format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.ERROR,  # 控制台打印的日志级别
                    filename='DownloadError.log',
                    filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(levelname)s: %(message)s'
                    # 日志格式
                    )


def open_html(url):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    # }

    html = requests.get(url).text  # 这里不加text返回<Response [200]>
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select("ul li div a img")
    i = 1
    # pic_no是照片文件夹序号
    pic_no = ""
    for li in lis:
        if i < 10:
            pic_no = "00" + repr(i)
        elif i < 100:
            pic_no = "0" + repr(i)
        elif i < 1000:
            pic_no = repr(i)
        load_image(li, pic_no)
        if i == 4:
            break
        i = i + 1


# 下载图片
def load_image(html, pic_no):
    regx = '<img alt="([\\s\\w\\-\\[\\]\\.\\《\\》\\！\\？\\～]+)" src="([\\s\\w\\:\\/\\.]+22359[\\s\\w\\:\\/\\.]+)" title="([\\s\\w\\-\\[\\]\\.\\《\\》\\！\\？\\～]+)"/>'
    pattern = re.compile(regx)
    get_image = re.findall(pattern, str(html))


    if get_image.__len__() > 0:
        info = get_image[0]
        # 图集名称
        title = get_image[0][0]
        # 图集编号
        pic_set_no = get_image[0][1].split("/")[5]
        num2 = 0
        # 图片编号
        num3 = ""
        while True:

            if num2 == 0:
                num3 = "0"
            elif num2 < 10:
                num3 = "00" + repr(num2)
            elif num2 < 100:
                num3 = "0" + repr(num2)
            elif num2 < 1000:
                num3 = repr(num2)
            # if pic_set_no != '29472' and (not flag):
            #     print("111111现在的图集编号是：" + pic_set_no + ", flag:" + repr(flag))
            #     break
            # elif pic_set_no == '29472':
            #     flag = True
            #     print("222222现在的图集编号是：" + pic_set_no + ", flag:" + repr(flag))
            #     break
            img = "https://t1.onvshen.com:85/gallery/22359/" + pic_set_no + "/" + num3 + ".jpg"

            require = urllib.request.Request(img)
            try:
                # 本项目目录
                # path = os.path.dirname(os.path.realpath(__file__)) + \
                #        "\\妲己_Toxic\\" + pic_no + "-" + pic_set_no + "-" + title + "\\"
                # 本地目录
                path = "E:\\妲己_Toxic\\" + pic_no + "-" + pic_set_no + "-" + title + "\\"
                y = os.path.exists(path)
                # 若保存目录不存在则创建目录
                if y != 1:
                    os.makedirs(path)
                pic_path = path + num3 + ".jpg"
                # 若图片存在则不再重复下载
                z = os.path.exists(pic_path)
                if z != 1:
                    repose = urllib.request.urlopen(require)
                    photo = repose.read()
                    with open(pic_path, 'wb') as f:
                        print('开始下载图片，图集名称：' + title + ", 图集编号：" + pic_set_no + ", 图片编号为" + num3)
                        f.write(photo)
                        f.close()
                        print('下载成功！！！')
                        time.sleep(0.5)
                num2 = num2 + 1

            except error.URLError as e:
                logging.error('下载失败，图集名称：' + title + ", 图集编号：" + pic_set_no + ", 图片编号为" + num3 + ", 失败原因:" + e.reason)
                break


def main():
    url = 'https://www.nvshens.com/girl/22359/album/'
    open_html(url)
    print("爬取完毕")


if __name__ == '__main__':
    main()
