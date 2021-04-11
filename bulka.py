import requests
from docx import Document
from bs4 import BeautifulSoup

token_test = '1739168654:AAEpDabUmUWuAJds56JrXAbKRUSNd88izOU'

def bulka():
    muk=[]
    response = requests.get('https://www.promtransbank.ru/')
    soup = BeautifulSoup(response.content, 'html.parser')
    suska = soup.find_all('div', class_="b-r-30 b-r-header g-png g-lightblue-bg")
    kek = soup.find_all('table', class_='b-currency-table b-table-noborder g-nulled-vspace')
    for data in suska:
        if soup.find_all('div', class_="b-r-30 b-r-header g-png g-lightblue-bg"):
            muk.append(data.text)
    for data in kek:
        if soup.find_all('table', class_='b-currency-table b-table-noborder g-nulled-vspace'):
            muk.append(data.text)
    new_list = [word for line in muk for word in line.split()]
    new_list.remove('Валюта')
    for ind in range(len(new_list)):
        if ind in[2]:
            new_list.insert(ind, '\n\n')
    for ind in range(len(new_list)):
        if ind in [5, 8, 12]:
            new_list.insert(ind, '\n\n')
    for ind in range(len(new_list)):
        if ind in[16]:
            new_list.insert(ind, '\n\n')
    for ind in range(len(new_list)):
        if ind in[6]:
            new_list.insert(ind, '\t\t\t\t\t\t\t\t\t\t\t\t')
    for ind in range(len(new_list)):
        if ind in[11,13]:
            new_list.insert(ind, '\t\t\t\t\t\t\t')
    for ind in range(len(new_list)):
        if ind in[17]:
            new_list.insert(ind, '\t\t\t\t\t\t\t')
    for ind in range(len(new_list)):
        if ind in[19]:
            new_list.insert(ind, '\t\t\t\t\t\t\t\t')
    for ind in range(len(new_list)):
        if ind in[8]:
            new_list.insert(ind, '\t\t\t')
    for ind in range(len(new_list)):
        if ind in[26]:
            new_list.insert(ind, '\t\t\t\t\t\t')
    for ind in range(len(new_list)):
        if ind in[25]:
            new_list.insert(ind, '\t')
    
    return '\t'.join(new_list)
