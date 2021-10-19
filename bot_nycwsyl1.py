""""Belirtilen site üzerinden web scraping yaparak istenen bölümü yazdıran yazılım."""
#Web scraping için BeautifulSoup ve requests kütüphaneleri import edildi.
#Log kontrolü için logging kütüphanesi import edildi ve try bloğu içine alındı.

try:
    from bs4 import BeautifulSoup
    import requests
    import logging
    import json
    import re
except ModuleNotFoundError:
    print("You have to install the required libraries".upper())
else:
    pass

logging.basicConfig(filename='test.log', level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s')

#BeautifulSoup ve requests kullanılarak we sayfasının istenen kısmı alındı
#ve text olarak tutuldu.
try:
    web_page = requests.get("https://www.nytimes.com/crosswords/game/mini")
except requests.exceptions.RequestException as my_error:
    print(my_error)


code_source = BeautifulSoup(web_page.content,"lxml")
total_area = code_source.find("section",attrs={"class":"Layout-clueLists--10_Xl"})
total_text = total_area.text
total_text = total_text.replace("Down","\nDown")

text1 = total_text[:total_text.find("Down")]
text2 = total_text[total_text.find("Down"):]

def visualize(my_text):
    """ Web sayfasından alınan bölümü istenen şekilde yazdıran fonksiyon"""
    my_new_text = ''
    for i in my_text:
        if i.isnumeric() and my_text.index(i)!=0:
            my_new_text += '\n' + i + '.' + ' '
        elif i.isnumeric() and my_text.index(i)==0:
            my_new_text += i + '.' + ' '
        elif not i.isnumeric():
            my_new_text += i
    logging.info(my_new_text)
    print(my_new_text)

visualize(total_text)

#JSON dosyası için fonksiyon define edildi ve .json dosyası oluşturuldu.
data = {}
def write_json(text):
    '''Ana texti ikiye bölüp bunları data listesine ekleyen fonksiyon'''
    res = re.split('(\d+)',text)
    data[res[0]]= []

    for i in range(1,len(res),2):
        across_element = {"number": res[i], "string": res[i+1]}
        data[res[0]].append(across_element)
    return data

mainContent = [
    write_json(text1),
    write_json(text2)
]

with open('data.json', 'w') as outfile: json.dump(mainContent, outfile)
        