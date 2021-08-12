import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://osu.ppy.sh/rankings/osu/performance?country=IN")
playerz = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
aaa = "<track -limit 50 "
for a in soup.findAll('a', href=True, attrs={'class':'ranking-page-table__user-link-text js-usercard'}):
	attr = a.attrs.get("class")[0]
	value = a.text
	players = value # this is the direct data im scraping from website (it has a lot of random spaces)
	player = players.strip() # stripped text
	playerz.append(player)
top1to10 = '"' + '" "'.join(playerz[0:10]) + '"'
top11to20 = '"' + '" "'.join(playerz[10:20]) + '"'
top21to30 = '"' + '" "'.join(playerz[20:30]) + '"'
top31to40 = '"' + '" "'.join(playerz[30:40]) + '"'
top41to50 = '"' + '" "'.join(playerz[40:50]) + '"'
f = open("output.txt", "w")
print(aaa + top1to10, file = f)
print(aaa + top11to20, file = f)
print(aaa + top21to30, file = f)
print(aaa + top31to40, file = f)
print(aaa + top41to50, file = f)
f.close()
driver.quit()