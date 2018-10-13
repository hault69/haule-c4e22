#1. download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs"

#1.1 connect to website
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()
#1.3 Decode data
webpage_text = raw_data.decode("utf8")

#1.4 save text
#w => write
#b => binary data thô

#2. extra ROI
#2.1 covert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
#print(soup.prettify())
ul = soup.find("section","section chart-grid")
ul_list = ul.find("ul")
li_list = ul_list.find_all("li")

news_list = []

for li in li_list:
    h3 = li.h3
    b = h3.a 
    song = b.string
    h4 = li.h4
    a = h4.a
    tilte = a.string
    print(tilte)
    print("----------------")
    print(song)
#     link = url+ a["href"]
#     #print(link)
#     news = OrderedDict({
#         "tilte": tilte,
#         "link": link,
#     })
#     news_list.append(news)

# #3. extra data
# pyexcel.save_as(records = news_list,dest_file_name = "dantri.xlsx")
