import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.alldatasheet.com/view.jsp?Searchword=LM324")

soup = BeautifulSoup(r.content, "html.parser")

print(soup.prettify())
s = soup.find_all("table", class_="width100yo")
print(s[0])
for row in s[0].find_all("tr"):
    cells = row.find_all("td")
    for cell in cells:
        a = cell.find_all("a")
        if len(a) > 0:
            print(cell)
            print(a[0]["href"][2:])
