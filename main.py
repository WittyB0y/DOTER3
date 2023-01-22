import eel
import requester as r
import wx

eel.init("web")


def reader(path: str) -> [str]:
    with open(path, 'r', encoding='utf-8') as file:
        file = map(lambda x: x.strip(), file.readlines())
    return list(file)


@eel.expose
def start(link: str, path):
    eel.writer('<div>Инициализация...</div>')
    file = reader(path)
    for data in file:
        data = data.split()
        eel.writer(f'<div>Авторизация {data[0].upper()}</div>')
        result = r.getData(link, data[0], data[1])
        if not result:
            eel.writer(f'<div>Не верный логин или пароль</div>')
        else:
            fileName = result[0]
            result = result[1]
            if len(result) > 0:
                eel.writer(f'<div>{result}</div>')
            else:
                eel.writer(f'<div>Нет данных</div>')
    return 'ok'


@eel.expose
def openFile(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return f'<div id="pathToFile">{path}</div>'


eel.start("main.html", size=(700, 700))
