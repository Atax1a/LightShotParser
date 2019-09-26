# libraries
import csv
from bs4 import BeautifulSoup as bs
import requests
import urllib
import itertools
from tqdm import tqdm as tq
# headers
headers = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
# base_url
combinations = []
# combinations
for i in itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyz1234567890',3):
    c = i[0]+i[1]+i[2]
    combinations.append(c)
# Folder path
directory = input('Full path to your folder -> ')
# Symbols for url
first_symbols = input('First symbols in url (exmpl: abc,ab,c & etc) -> ')
base_urlc = 'https://prnt.sc/' + first_symbols
# Amount of images
iterations = int(input('Amount of images -> '))


def lightshot_parse(base_urlc, headers):
    for i in tq(range(0,iterations)):
        try:
            base_url =base_urlc + combinations[i]
            session = requests.Session()
            request = session.get(base_url,headers = headers)
            if request.status_code == 200:
                # parsing
                soup = bs(request.content,'html.parser')
                img_div = str(soup.findAll('div', attrs = {'class':'image-container image__pic js-image-pic'}))

                # finding the url
                url_start = img_div.find('src="',0,len(img_div))+5;
                url_end = img_div.find('"',url_start,len(img_div))
                img_url = img_div[url_start:url_end]

                # naming the images
                img_dir = directory + '\\' + str(i)+'.png'

                # saving the image

                img = urllib.request.urlopen(img_url).read()
                img_file = open(img_dir,'wb')
                img_file.write(img)
                img_filre.close()

            else:
                print('ERROR')
        except:
            pass
        else:
            continue


print(lightshot_parse(base_urlc,headers))
