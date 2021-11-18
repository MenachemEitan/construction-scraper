from requests_html import HTMLSession
from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
import re



def getdata_baterii():
    s = HTMLSession()
    filename = "batarii.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_baterii = 'https://www.dedeman.ro/ro/baterii/c/67'
    temp_baterii = 'https://www.dedeman.ro/ro/baterii/c/67?page='
    for g in range(19):
        if g == 0:
            url = my_url_baterii
        else:
            url = temp_baterii+str(g+1)
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
        for i in range(len(proudukt_boxs)):
            box = proudukt_boxs[i]
            # print(box.a['title'])
            box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
                1].text
            # print("price " ,box_price)
            box_img = box.a.span.span.img["src"]
            # print(box_img)
            f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                box_img).replace(",", "|") + '\n')

    return

def getdata_mobilier_baie():
    s = HTMLSession()
    filename = "mobiliar_baie.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_baterii = 'https://www.dedeman.ro/ro/mobilier-baie/c/65'
    temp_baterii = 'https://www.dedeman.ro/ro/mobilier-baie/c/65?page='
    for g in range(9):
        if g == 0:
            url = my_url_baterii
        else:
            url = temp_baterii + str(g + 1)
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
        for i in range(len(proudukt_boxs)):
            box = proudukt_boxs[i]
            # print(box.a['title'])
            box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
                1].text
            # print("price " ,box_price)
            box_img = box.a.span.span.img["src"]
            # print(box_img)
            f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                box_img).replace(",", "|") + '\n')

    return

def getdata_iluminat_pentru_baie():
    s = HTMLSession()
    filename = "iluminat_pentru_baie.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_baterii = 'https://www.dedeman.ro/ro/iluminat-pentru-baie/c/1035'
    temp_baterii = 'https://www.dedeman.ro/ro/iluminat-pentru-baie/c/1035'
    # for g in range(1):
    #     if g == 0:
    #         url = my_url
    #     else:
    #         url = temp + str(g + 1)

    uClient = uReq(my_url_baterii)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
    for i in range(len(proudukt_boxs)):
        box = proudukt_boxs[i]
        # print(box.a['title'])
        box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
            1].text
        # print("price " ,box_price)
        box_img = box.a.span.span.img["src"]
        # print(box_img)
        f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
            box_img).replace(",", "|") + '\n')

def getdata_oglinzi_baie_cu_polita():
    s = HTMLSession()
    filename = "oglinzi_baie_cu_polita.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_oglinzi_baie_cu_polita = 'https://www.dedeman.ro/ro/oglinzi-baie-cu-polita/c/446'
    temp_oglinzi_baie_cu_polita = 'https://www.dedeman.ro/ro/oglinzi-baie-cu-polita/c/446'
    # for g in range(1):
    #     if g == 0:
    #         url = my_url
    #     else:
    #         url = temp + str(g + 1)

    uClient = uReq(my_url_oglinzi_baie_cu_polita)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
    for i in range(len(proudukt_boxs)):
        box = proudukt_boxs[i]
        # print(box.a['title'])
        box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
            1].text
        # print("price " ,box_price)
        box_img = box.a.span.span.img["src"]
        # print(box_img)
        f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
            box_img).replace(",", "|") + '\n')

def getdata_cazi_si_cabine_cu_hidromasaj():
    s = HTMLSession()
    filename = "cazi_si_cabine_cu_hidromasaj.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_cazi_si_cabine_cu_hidromasaj = 'https://www.dedeman.ro/ro/cazi-si-cabine-cu-hidromasaj/c/71'
    temp_cazi_si_cabine_cu_hidromasaj = 'https://www.dedeman.ro/ro/cazi-si-cabine-cu-hidromasaj/c/71?page='
    for g in range(2):
        if g == 0:
            url =  my_url_cazi_si_cabine_cu_hidromasaj
        else:
            url = temp_cazi_si_cabine_cu_hidromasaj
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
        for i in range(len(proudukt_boxs)):
            box = proudukt_boxs[i]
            # print(box.a['title'])
            box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
                1].text
            # print("price " ,box_price)
            box_img = box.a.span.span.img["src"]
            # print(box_img)
            f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                box_img).replace(",", "|") + '\n')

def cabine_si_cadite_de_dus():
    s = HTMLSession()
    filename = "cabine_si_cadite_de_dus.csv"
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    my_url_baterii = 'https://www.dedeman.ro/ro/cabine-si-cadite-de-dus/c/70'
    temp_baterii = 'https://www.dedeman.ro/ro/cabine-si-cadite-de-dus/c/70?page='
    for g in range(9):
        if g == 0:
            url = my_url_baterii
        else:
            url = temp_baterii + str(g + 1)
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
        for i in range(len(proudukt_boxs)):
            box = proudukt_boxs[i]
            # print(box.a['title'])
            box_price = box.find_all("span", {"class": "bold"})[0].text + box.find_all("span", {"class": "bold"})[
                1].text
            # print("price " ,box_price)
            box_img = box.a.span.span.img["src"]
            # print(box_img)
            f.write(str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                box_img).replace(",", "|") + '\n')







getdata_baterii()
getdata_mobilier_baie()
getdata_iluminat_pentru_baie()
getdata_oglinzi_baie_cu_polita()
getdata_cazi_si_cabine_cu_hidromasaj()
cabine_si_cadite_de_dus()














