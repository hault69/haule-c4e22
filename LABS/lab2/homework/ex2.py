from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

webpage_text = raw_data.decode("utf-8")

soup = BeautifulSoup(webpage_text, "html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = div.table
tr_list = table.find_all("tr")
news_list = []
for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        names = td_list[0].string
        quy1 = td_list[1].string
        quy2 = td_list[2].string
        quy3 = td_list[3].string
        quy4 = td_list[4].string
        new = OrderedDict({
            'Name': names,
            'Quý 1 - 2017': quy1,
            'Quý 2 - 2017': quy2,
            'Quý 3 - 2017': quy3,
            'Quý 4 - 2016': quy4,
        })
    news_list.append(new)
pyexcel.save_as(records = news_list, dest_file_name = "hoatdongkinhdoanh.xlsx")