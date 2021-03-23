from subprocess import call
import requests
#call(["textutil", "-convert", "txt", "130_BD"])

token = '*'

data = {
    '110-БД' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БД.rtf',
    '110-БМ-1' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БМ-1.rtf',
    '110-БМ-2' : 'http://www.fa.ru/fil/ufa/student/Bak_och/110БМ-2.rtf',
    '110-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/110БУ.rtf',
    '120-БД': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БД.rtf',
    '120-БИ': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БИ.rtf',
    '120-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БУ.rtf',
    '120-БМО': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БМО.rtf',
    '120-БМФ': 'http://www.fa.ru/fil/ufa/student/Bak_och/120БМФ.rtf',
    '130-БД': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БД.rtf',
    '130-БM': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БМ.rtf',
    '130-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БУ.rtf',
    '140-БД': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БД.rtf',
    '140-БМ': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БМ.rtf',
    '140-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БУ.rtf',
    '140-ЭБ': 'http://www.fa.ru/fil/ufa/student/Bak_och/140ЭБ.rtf'
}


url = 'http://www.fa.ru/fil/ufa/student/Bak_och/130БД.rtf'

def download_data(name):
    r = requests.get(url, allow_redirects=True)
    open(name,"wb").write(r.content)
    call(["textutil", "-convert", "txt", str(name)])

def schedule(text):
    a = []
    a_file = open(text, "r")
    lines = a_file.readlines()
    del lines [:4]
    new_file = open("text_e.txt", "w+")
    for line in lines:
        new_file.write(line)
        a.append(line)
    return(a)

print(schedule('130_Bd.txt'))