import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cotacao+dolar"
requisicao = requests.get(link)

print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")

titulo = site.find("input")
# print(site.prettify())
print(titulo)