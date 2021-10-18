#Web scraping için BeautifulSoup ve requests kütüphaneleri import edildi.
#Log kontrolü için logging kütüphanesi import edildi ve try bloğu içine alındı. 
try:
    from bs4 import BeautifulSoup
    import requests
    import logging
except ModuleNotFoundError:
    print("You have to install the required libraries".upper())
else:
    pass

#BeautifulSoup ve requests kullanılarak we sayfasının istenen kısmı alındı
#ve text olarak tutuldu.

web_page = requests.get("https://www.nytimes.com/crosswords/game/mini")
code_source = BeautifulSoup(web_page.content,"lxml")

total_area = code_source.find("section",attrs={"class":"Layout-clueLists--10_Xl"})

total_text = total_area.text
total_text = total_text.replace("Down","\nDown")
# Text'i istenen şekilde görüntülemek için function define edildi.

def visualize(my_text):
    my_new_text = ''
    for i in range(0,len(my_text)):
        if my_text[i].isnumeric() == True and i!=0:
            my_new_text += '\n' + my_text[i] + '.' + ' '
        elif my_text[i].isnumeric() == True and i==0:
            my_new_text += my_text[i] + '.' + ' '
        elif my_text[i].isnumeric() == False:
            my_new_text += my_text[i]
    print(my_new_text)

visualize(total_text)