# crawler công cụ lấy dữ liệu mới về 
# crawler - lây HTML
# Muc tieu: Crwl muc suc khoe cua dantri.vn
import requests
# --> Khai báo thư viện sẽ dùng là gì
url = "https://dantri.com.vn/suc-khoe.htm"
response = requests.get(url)
# print(response.content.decode('utf-8'))

