from requests_html import HTMLSession
from urllib.request import urlopen as uReq
from bs4 import  BeautifulSoup as soup
import re




def geturls(sursurl):
    uClient = uReq(sursurl)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    urls = page_soup.find_all("a", {"class": "subcategory-box landing-page-zone-box"})
    return urls


def get_data(sursurl,filename ):
    f = open(filename, "w")
    headers = "produkt, price, imge\n"
    f.write(headers)
    urls = geturls(sursurl)
    print(len(urls), "len urls")
    for i in range(len(urls)):
        first_temp_url = 'https://www.dedeman.ro'+urls[i]['href']
        print(i, "sub_categori", first_temp_url)
        uClient = uReq(first_temp_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        page_nums = page_soup.find_all("div", {"class": "pagination-list-wrap"})
        if len(page_nums) !=0:
            page_num = len(page_nums[0].find("ul", {"class": "inline-list pagination-list"}))
            print(page_num, "len  page num")
            for g in range(page_num):
                if g == 0:
                    url = first_temp_url
                else:
                    url = first_temp_url+"?page=" +str(g+1)
                # print(url)
                try:
                    uClient = uReq(url)
                    page_html = uClient.read()
                    uClient.close()
                    page_soup = soup(page_html, "html.parser")
                    proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
                    # print(len(proudukt_boxs), "len_proudukt_boxs ")
                    for i in range(len(proudukt_boxs)):
                        box = proudukt_boxs[i]
                        # print(box.a['title'])
                        box_price = box.find_all("span", {"class": "bold"})[0].text + \
                                    box.find_all("span", {"class": "bold"})[
                                        1].text
                        # print("price " ,box_price)
                        box_img = box.a.span.span.img["src"]
                        # print(box_img)
                        f.write(
                            str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                                box_img).replace(",", "|") + '\n')

                    print(url, "good url")
                except:
                    print('ldaijpajv',url, "bed url")
        else:
            url = first_temp_url
            try:
                uClient = uReq(url)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, "html.parser")
                proudukt_boxs = page_soup.find_all("div", {"class": "product-box"})
                # print(len(proudukt_boxs), "len_proudukt_boxs ")
                for i in range(len(proudukt_boxs)):
                    box = proudukt_boxs[i]
                    # print(box.a['title'])
                    box_price = box.find_all("span", {"class": "bold"})[0].text + \
                                box.find_all("span", {"class": "bold"})[
                                    1].text
                    # print("price " ,box_price)
                    box_img = box.a.span.span.img["src"]
                    # print(box_img)
                    f.write(
                        str(box.a['title']).replace(",", "|") + "," + str(box_price).replace(",", "|") + "," + str(
                            box_img).replace(",", "|") + '\n')

                print(url, "good url")
            except :
                print( "ldaijpajv'avjaivjivjv",url, "bed url")






get_data('https://www.dedeman.ro/ro/gradina/c/17','dedeman_Toamna.csv')
get_data('https://www.dedeman.ro/ro/mobila/c/16','dedemab_mobila.csv')
get_data('https://www.dedeman.ro/ro/baie/c/1528','dedeman_baie.csv' )
get_data('https://www.dedeman.ro/ro/scule-si-unelte/c/6','scule_si_unelte.csv')
get_data('https://www.dedeman.ro/ro/bucatarie/c/1520','dedeman_bucatarie.csv')
get_data('https://www.dedeman.ro/ro/electrocasnice/c/32','dedeman_electrocasnice.csv')
get_data('https://www.dedeman.ro/ro/gradina/c/17','dedeman_gradina.csv')
get_data('https://www.dedeman.ro/ro/auto/c/19','dedeman_auto.csv')
get_data('https://www.dedeman.ro/ro/decoratiuni/c/34','dedeman_decoratiuni.csv')
get_data('https://www.dedeman.ro/ro/amenajari-interioare/c/7','dedemen_amenajari_interioare.csv')
get_data('https://www.dedeman.ro/ro/gresie-si-faianta/c/1068','dedemen_gresie_si_faianta.csv')
get_data('https://www.dedeman.ro/ro/constructii/c/1426','dedeman_constructii.csv')
get_data('https://www.dedeman.ro/ro/termice/c/4','dedeman_termice.csv')
get_data('https://www.dedeman.ro/ro/electrice/c/62','dedeman_electrice.csv')
get_data('https://www.dedeman.ro/ro/sanitare/c/1427','dedeman_sanitare.csv')
get_data('https://www.dedeman.ro/ro/dormitoare/c/1590','dedeman_dormitoare.csv')











