import requests
from bs4 import BeautifulSoup

url = "https://pdf1.alldatasheet.com/datasheet-pdf/download/17871/PHILIPS/LM324.html"
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.content, "html.parser")
    security_code = ""
    for td in soup.find_all("td", {"bgcolor": "#eeeeee"}):
        security_code += td.text
    print(security_code)
else:
    print("Security code not found.")
