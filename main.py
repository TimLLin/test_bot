from subprocess import call
import requests
#call(["textutil", "-convert", "txt", "130_BD"])

token = '**'

url = 'http://www.fa.ru/fil/ufa/student/Bak_och/130БД.rtf'

def download_data(name):
    r = requests.get(url, allow_redirects=True)
    open(name,"wb").write(r.content)
    call(["textutil", "-convert", "txt", str(name)])

def schedule(text):
    a_file = open(text, "r")
    lines = a_file.readlines()
    del lines [:4]
    new_file = open("text_e.txt", "w+")
    for line in lines:
        new_file.write(line)
        a = []
        a.append(line)
    return a


#download_data('130_BD')
#schedule('130_BD.txt')
