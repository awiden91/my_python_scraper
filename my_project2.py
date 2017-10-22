# I need ot import the modules for requests and parsing html
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# url I need to request
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a", {"class": "item-title"})

    product_name = title_container[0].text

    Shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = Shipping_container[0].text.strip()

print("brand: " + brand)
print("product_name " + product_name)
print("shipping: " + shipping
