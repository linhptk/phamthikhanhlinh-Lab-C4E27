from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection = urlopen(url)
raw_data = connection.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content,"html.parser")    
with open("Baocao.html", "wb") as f:
    f.write(raw_data)
table = soup.find("table", id="tableContent")
tr_list = table.find_all("tr")
# print(tr_list[0].prettify())

list_bang_bao_cao = []

for tr in tr_list:
    dic_so_lieu_bao_cao = OrderedDict({})
    td_list = tr.find_all("td")

    for i in td_list:
        if i ==0:
            dic_so_lieu_bao_cao["Tieu de"] = td_list[i].string
        elif i ==1:
            dic_so_lieu_bao_cao["Quy 4 -2016"] = td_list[i].string
        elif i ==2:
            dic_so_lieu_bao_cao["Quy 1 -2017"] = td_list[i].string
        elif i ==3:
            dic_so_lieu_bao_cao["Quy 2 -2017"] = td_list[i].string
        elif i ==4:
            dic_so_lieu_bao_cao["Quy 3 -2017"] = td_list[i].string
    list_bang_bao_cao.append(dic_so_lieu_bao_cao)
    print(list_bang_bao_cao)
# pyexcel.save_as(records=list_bang_bao_cao, dest_file_name="List_bang_bao_cao.xlsx")   


