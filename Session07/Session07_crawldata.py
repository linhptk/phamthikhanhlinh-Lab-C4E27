from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
# phan du lieu lay ve là ROI
# 1.Create connection
url = "https://dantri.com.vn/"
connection = urlopen(url)
# ---> mở đường cho dữ liệu về máy
# 1.1. Download page
raw_data = connection.read()
html_content = raw_data.decode('utf-8')
# print(html_content)
# 2. Find ROI
# Nên Đặt tên biến trùng với tên thẻ
# soup = BeautifulSoup(html_content,"html.parser")
# ul = soup.find("ul", "ul1 ulnew")

# # print(a.prettify())
# # for li in li_list:
#     # print("*" *50)
# # tên thẻ: ul
# # tên class: ul1 ulnew
# # id: ul = soup.find("ul", id="ul1 ulnew")

# # 3. Extract ROI
# li_list = ul.find_all("li")
# # data =[]
# news_list = []
# for li in li_list:
#     # li = li_list[0]
#     # post={}

#     h4 = li.h4
#     a = h4.a
#     # post["title"] = a.string
#     title = a.string
#     link = url + a["href"]
#     news = OrderedDict({
#         "Title": title.lstrip().rstrip(),
#         "Link" : link,
#         })
#     news_list.append(news)
#     # print(news_list)
#     # post["link"] = url + a["href"]
#     # data.append(post)
#     # print(title.lstrip())
#     # print(link)
#     # print("*" * 50)
# # pyexcel.save_as(records=data, dest_file_name="dantri.xls")
# # 4. Save data
#  

with open("dantri.html", "wb") as f:
    f.write(raw_data)