import eel, pyperclip as copytext
import requester as r
import filter as filtertools
from playsound import playsound
from solver import fillFunc
import tkinter as tk
from tkinter import filedialog

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
def openFile():
    root = tk.Tk()
    root.attributes("-topmost", True)
    path = filedialog.askopenfilename(filetypes=(('text', '*.txt'),))
    root.destroy()
    if len(path) < 1 or path is None:
        return '<div id="pathToFile" class="notification">Не выбран файл!</div>'
    return f'<div id="pathToFile" class="notification">{path}</div>'


eel.start("main.html", size=(700, 700))
