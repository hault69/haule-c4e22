from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

raw_data = conn.read()

webpage_text = raw_data.decode("utf-8")

# f = open("itunes.html", "wb")
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(webpage_text, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.div
ul = div.ul
li_list = ul.find_all("li")
news_list = []
for li in li_list:
    a = li.h3.a
    names = a.string
    a = li.h4.a
    artists = a.string
    
    new = OrderedDict({
        'Name': names,
        'Artist': artists,
    })
    news_list.append(new)

pyexcel.save_as(records = news_list, dest_file_name = "TopSongItunes.xlsx")



for i in news_list:
    searchs = i['Name'] + i['Artist']

    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([searchs])