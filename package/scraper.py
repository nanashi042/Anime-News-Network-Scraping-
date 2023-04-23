from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.animenewsnetwork.com")
soup = BeautifulSoup(data.text, 'html.parser')

def get_image():
    img_lst = []
    mydivs = soup.findAll("div", {"class": "cover-image lazyload"})

    for img in mydivs:
        img_lst.append(img['data-src'])

    return img_lst

def get_name():
    mydivs = soup.findAll("div", {"class": "overlay"})
    name_list = []
    split_list = []
    names  = " "
    for i in range(5):
        names = mydivs[i].text
        name_list.append(names.split(","))
    return name_list

names = get_name()
print(names[1])