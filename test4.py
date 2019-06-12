import os
import re

str = '<img alt="《尤蜜荟》2018年写真精选合集" src="https://img.onvshen.com:85/gallery/20763/29203/cover/0.jpg" title="《尤蜜荟》2018年写真精选合集"/>'
regx = '<img alt="([\\s\\w\\-\\[\\]\\.\\《\\》\\！\\？\\～]+)"' +\
          ' src="([\\s\\w\\:\\/\\.]+22359[\\s\\w\\:\\/\\.]+)"' + \
          ' title="([\\s\\w\\-\\[\\]\\.\\《\\》\\！\\？\\～]+)"/>'
pattern = re.compile(regx)
get_image = re.findall(pattern, repr(str))
# print(get_image)
# for ss in get_image:
#     for s in ss:
#         print(s)
print(os.path.dirname(os.path.realpath(__file__)))
