import requests
from bs4 import BeautifulSoup

puanurl = "http://www.tff.org/default.aspx?pageID=198"

req = requests.get(puanurl)

soup = BeautifulSoup(req.content,"html.parser")

gelen_bilgi = soup.find_all("div",{"id":"ctl00_MPane_m_198_1890_ctnr_m_198_1890_Panel1"})

puan_tablosu = (gelen_bilgi[0].contents)[len(gelen_bilgi[0].contents)-2]

takim_ismi = puan_tablosu.find_all("a")
puan_durumu = puan_tablosu.find_all("span")


pd = 15
x = 0
while(pd >= 15 ):
    while(x <= 18):
        print(takim_ismi[x].text)
        print("Puanı =>"+puan_durumu[pd].text)
        print("*********************************************")
        x+=1
        pd+=8
