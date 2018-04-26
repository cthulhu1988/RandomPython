
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

myUrl = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48'

uClient = uReq(myUrl)

page_html = uClient.read()

uClient.close()

fileName = "cards.csv"
f = open(fileName, "w")

headers = "brand, product_name, price\n"


f.write(headers)


page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class": "item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class": "price-ship"})
	shipping = shipping_container[0].text.strip()
	price_container = container.find("div")
	priceLi = price_container("li")
	priceSpan = priceLi.span
	price = priceSpan
	print(price)


	f.write(brand + "," + product_name + "," + shipping + "\n")
f.close()