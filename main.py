import requests
from docx import Document
from bs4 import BeautifulSoup
data = {
    '110-БД.docx' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БД.docx',
    '110-БМ-1.docx' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БМ-1.docx',
    '110-БМ-2.docx' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БМ-2.docx',
    '110-БУ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/110БУ.docx',
    '120-БД.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БД.docx',
    '120-БИ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БИ.docx',
    '120-БУ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БУ.docx',
    '120-БМО.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БМО.docx',
    '120-БМФ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БМФ.docx',
    '130-БД.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БД.docx',
    '130-БМ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БМ.docx',
    '130-БУ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БУ.docx',
    '140-БД.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БД.docx',
    '140-БМ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БМ.docx',
    '140-БУ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БУ.docx',
    '140-ЭБ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/140ЭБ.docx'
}


def download_data(name,url):
    r = requests.get(url, allow_redirects=True)
    open(name, "wb").write(r.content)
    file = open(name, 'rb')
    return file

def w_schedule(text):
    sch = [[],[],[],[],[]]
    date = ['ПН','ВТ','СР','ЧТ','ПТ']
    document = Document(text)
    fulltext = []
    for para in document.paragraphs:
        fulltext.append(para.text)
    new_list = [word for line in fulltext for word in line.split()]
    sch[0] = new_list[new_list[:].index("ПН")-1:new_list[:].index("ВТ")-1]
    sch[1] = new_list[new_list[:].index("ВТ")-1:new_list[:].index("СР")-1]
    sch[2] = new_list[new_list[:].index("СР")-1:new_list[:].index("ЧТ")-1]
    sch[3] = new_list[new_list[:].index("ЧТ")-1:new_list[:].index("ПТ")-1]
    sch[4] = new_list[new_list[:].index("ПТ")-1:]
    return sch

def news():
    n=[]
    response = requests.get("http://www.fa.ru/fil/ufa/News/Forms/AllPages.aspx#InplviewHashb8d04cfc-441e-4048-ac3b-413a847304ad=FilterField1%3DCategory-FilterValue1%3D%25D0%259D%25D0%25BE%25D0%25B2%25D0%25BE%25D1%2581%25D1%2582%25D0%25B8%2520%25D0%25A3%25D0%25BD%25D0%25B8%25D0%25B2%25D0%25B5%25D1%2580%25D1%2581%25D0%25B8%25D1%2582%25D0%25B5%25D1%2582%25D0%25B0")
    soup = BeautifulSoup(response.content, 'html.parser')
    div_title = soup.find_all('td', class_="ms-vb2")
    for element in div_title:
        if soup.find_all('div', class_='ms-rtestate-field'):
            n.append(element.text)
    n.remove('Новости Университета')
    for elem in range(len(n)):
        if n[elem]=="":
            n[elem]="\n"
    return n
