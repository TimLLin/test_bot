import requests

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
    '130-БМ': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БМ.rtf',
    '130-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/130БУ.rtf',
    '140-БД': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БД.rtf',
    '140-БМ': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БМ.rtf',
    '140-БУ': 'http://www.fa.ru/fil/ufa/student/Bak_och/140БУ.rtf',
    '140-ЭБ.docx': 'http://www.fa.ru/fil/ufa/student/Bak_och/График%20пересдач.docx'
}


def download_data(name,url):
    r = requests.get(url, allow_redirects=True)
    open(name, "wb").write(r.content)


download_data('130БД.doc','http://www.fa.ru/fil/ufa/student/Bak_och/130БД.doc')
