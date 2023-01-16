import requests
from bs4 import BeautifulSoup
from rich.table import Table
from rich import box
from rich.console import Console

console = Console()

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
print(rowlist[1:])
table = Table(title="yeahh", show_lines=True)
table.add_column("Manufacturer", style="blue")
table.add_column("Link to pdf")
for x in rowlist[1:]:
    if "www." not in x[0]:
        table.add_row(x[0], f'[link="{x[1]}]{x[1]}[/link]')

console.print(table)
