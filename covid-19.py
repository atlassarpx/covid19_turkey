import requests
from bs4 import BeautifulSoup
import os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

r = requests.get('https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html/')
soup = BeautifulSoup(r.content, "html.parser")
all_datas = soup.find_all("script")
index_datas = all_datas[11]
index_datas = str(index_datas)
datas = index_datas.split('"')
test = datas[9]
case = datas[13]
sick = datas[17]
die = datas[21]
heal = datas[25]

print("Test Sayısı:         {}".format(test))
print("Vaka Sayısı:         {}".format(case))
print("Vefat Sayısı:        {}".format(die))
print("İyileşen Sayısı:     {}".format(heal))
print("Ağır Hasta Sayısı:   {}".format(sick))
