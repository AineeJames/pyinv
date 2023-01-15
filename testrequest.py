import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.alldatasheet.com/view.jsp?Searchword=LM324")

soup = BeautifulSoup(r.content, "html.parser")

soup = soup.find_all("div", class_="overflowyo")[2]
s = soup.find_all("table", class_="main")
rowlist = []
counter = 0
for row in s[0].find_all("tr"):
    cells = row.find_all("td")
    rowlist.append([])
    for cell in cells:
        a = cell.find_all("a")
        if len(a) > 0:
            rowlist[counter].append(a[0]["href"][2:])
        else:
            rowlist[counter].append(cell.text)
    counter += 1
print(rowlist)
