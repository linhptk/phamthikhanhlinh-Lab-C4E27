from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs"
connection = urlopen(url)
raw_data = connection.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section", "section chart-grid")
li_list = section.div.ul.find_all("li")
li = li_list[0]
# print(li)
# print(li.prettify())
song_list = []
for li in li_list:
    song = {}
    h3 = li.h3
    h4 = li.h4

    names = h3.string
    artists = h4.string
    song = OrderedDict({
        "Names": names,
        "Artists": artists
            })
    song_list.append(song)
print(song_list)
pyexcel.save_as(records=song_list, dest_file_name="Song_list_iTunes.xlsx")


download_song_list = []
for i in song_list:
    new_song_list = i['Names']+''+i['Artists']
    download_song_list.append(new_song_list)

options = {
    'default_search': 'ytsearch', 
    'max_downloads': len(download_song_list) 
}
dl = YoutubeDL(options)
dl.download(download_song_list)
