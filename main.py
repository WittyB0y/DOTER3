import eel
import wx
import filter as filtertools
import requester as r

eel.init("web")


def reader(path: str) -> [str]:
    with open(path, 'r', encoding='utf-8') as file:
        file = map(lambda x: x.strip(), file.readlines())
    return list(file)


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
        else:
            eel.writer(f'<div class="notification">Нет данных</div>')
    try:
        return f'<div class="notification">Сбор завершён</div><div class="notification">Вопросы сохранены в:<div class="notification" id="filePathTag">{fileName}</div></div><div id="delBtnHandler"><button id="submitDelete" onclick="deleteDub()">Удалить дубликаты</button></div>'
    except UnboundLocalError as e:
        return f'<div class="notification">Сбор завершён</div>'


@eel.expose
def deleteDub(path: str):
    eel.writer(f'<div class="notification attetion">Удаление дубликатов запущено</div>')
    filtertools.main(path)
    return 'ok'


@eel.expose
def openFile(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = 'Не выбран файл!'
    dialog.Destroy()
    return f'<div id="pathToFile" class="notification">{path}</div>'


eel.start("main.html", size=(700, 700))
