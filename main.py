import eel
import wx
import filter as filtertools
import requester as r
from playsound import playsound
from solver import fillFunc
import pyperclip as copytext

eel.init("web")


@eel.expose
def funcToСlipboard(path):
    data = reader(path)
    res = fillFunc(data)
    copytext.copy(res)


def reader(path: str) -> [str]:
    with open(path, 'r', encoding='utf-8') as file:
        file = map(lambda x: x.strip(), file.readlines())
    return list(file)


#
@eel.expose
def start(link: str, path: str) -> str:
    eel.writer('<div class="notification">Инициализация...</div>')
    file = reader(path)
    for data in file:
        data = data.split()
        eel.writer(f'<div class="notification">Авторизация {data[0].upper()}</div>')
        result = r.getData(link, data[0], data[1], eel.writer)
        if isinstance(result, bool):
            continue
        fileName = result[0]
        result = result[1]
        if len(result) > 0:
            eel.writer(f'<div>{result}</div>')
        # else:
        #     eel.writer(f'<div class="notification error">Нет данных</div>')
    try:
        eel.writer(
            f'<div class="notification">Сбор завершён</div><div class="notification">Вопросы сохранены в:<div '
            f'class="notification" id="filePathTag">{fileName}</div></div><div id="delBtnHandler"><button '
            f'id="submitDelete" onclick="deleteDub()">Удалить дубликаты</button></div>')
        playsound("web\\audio\\notification_sound.mp3", block=True)
    except UnboundLocalError as e:
        return f'<div class="notification">Сбор завершён</div>'


@eel.expose
def deleteDub(path: str):
    output = filtertools.main(path)
    eel.writer('<div class="notification attetion">Дубликаты удалены</div>')
    eel.writer(f'<div class="notification attetion">Файл содержит {output[0]} уникальных вопроса</div><div '
               f'class="notification">Вопросы сохранены в:<div class="notification" id="filePathTag"><div '
               f'class="fileSaved" id="uniSavedFile">{output[1]}</div></div></div>'
               f'<div id="divbtnfunc"><button id="funcToClipboard" onclick="readSavedFileName(1)">Скопировать код в буфер обмена</button></div>')


@eel.expose
def openFile(wildcard="*.txt"):
    app = wx.App(None)
    style = (wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        dialog.Destroy()
        path = 'Не выбран файл!'
        return f'<div class="notification error">{path}</div>'
    dialog.Destroy()
    return f'<div id="pathToFile" class="notification">{path}</div>'


eel.start("main.html", size=(700, 700))
