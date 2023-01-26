import requests as r
from bs4 import BeautifulSoup as bs
import lxml

globAuthLink = 'http://dot3.gsu.by/login/index.php'


def getCsrf() -> tuple():
    """Get CSRF to auth"""
    ses = r.session()
    getElements = bs(ses.get(globAuthLink).content, 'lxml')
    try:
        return getElements.select_one('input[name=logintoken]')['value'], ses  # tuple with csrf and session
    except TypeError as e:
        return '0', ses


def auth(link: str, login: str, password: str, data: tuple, writer) -> list:
    csrf = data[0]
    session = data[1]

    authData = {
        "logintoken": csrf,
        "username": login,
        "password": password,
        "rememberusername": 1
    }
    checkForNotAuth = session.post(globAuthLink, data=authData)
    if bs(checkForNotAuth.content, 'lxml').select_one('div[class="alert alert-danger"]'):  # if this elemet exists it
        # means wrong login and password
        return writer(f'<div class="notification emodzi"><p>Не верный логин или пароль</p><p>🚫</p></div>')
    result = bs(session.get(link, data={'id': link[link.rfind('=') + 1:]}).content, 'lxml')
    links = [x.a['href'] for x in result.select('td[class="cell c4 lastcol"]') if x.a is not None]
    if len(links) == 0:
        links = [x.a['href'] for x in result.select('td[class="cell c3 lastcol"]') if x.a is not None]
    return links, session


def writer(questions, h1, score, corr, uncorr):
    nameFile = "_".join(h1.split())[:30] + '.txt'
    if questions is not None:
        with open(nameFile, 'a', encoding='utf-8') as f:
            for q in questions:
                f.write(q[0] + '\n' + q[1] + '\n')
    return f'Правильных ответов: {corr}<p>🟢</p></div><div class="emodzi">Неправильных ответов: {uncorr}<p>🔴</p></div><div>Результат: {score}</div></div>', nameFile


def getQuestions(datas: lxml):
    allData = []
    h1 = datas.h1.text.strip()
    score = datas.select_one('tbody').text
    score = score[score.rfind('Оценка') + 6:]
    correction = [x.text.strip() for x in datas.find_all(
        'div', {'grade', 'qtext'})]
    answers = datas.find_all('div', {'r0', 'r1', 'r2', 'r3'})
    all_answ = [x.text.strip() for x in answers if 'checked' in str(x)]
    grade = [correction[x] for x in range(0, (len(correction)), 2)]
    if len(all_answ) != len(grade):
        return ['Пустой тест', '-']
    quests = [correction[x] for x in range(1, (len(correction)), 2)]
    v = 0
    corr = 0
    uncorr = 0
    for time in range(0, len(quests)):
        if quests[v] not in allData:
            if grade[v] in ('Баллов: 0,00 из 1,00', 'Баллов: 0 из 1'):
                allData.append([quests[v], '---' + all_answ[v]])
                uncorr += 1
            else:
                allData.append([quests[v], '+++' + all_answ[v]])
                corr += 1
        v += 1
    return writer(allData, h1, score, corr, uncorr)


def getTest(data, writer):
    res_data = ''
    if callable(data):
        return False
    session = data[1]
    links = data[0]
    for t, link in enumerate(links):
        payload = {
            'attempt': link[link.find('=') + 1:link.rfind('&')],
            'cmid': link[link.rfind('=') + 1:]
        }
        allTest = bs(session.get(link, data=payload).content, 'lxml')
        data = getQuestions(allTest)
        writer(f'<div class="notification"><div class="emodzi">{t + 1}. {data[0]}')
        result = f'<div class="fileSaved">{data[1]}</div>'
    return result, res_data


def getData(link: str, login: str, password: str, writer) -> lxml or bool:
    data = getCsrf()
    if data == 'error3':
        return 'error3'
    getAuth = auth(link, login, password, data, writer)
    return getTest(getAuth, writer)
