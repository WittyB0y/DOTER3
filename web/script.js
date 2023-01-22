eel.expose(writer);
function writer(data) {
    document.getElementById('info').innerHTML += data;
}
async function getLink() {
    let link = document.getElementById('link').value;
    let path = document.getElementById('pathToFile');
    destroyer()

    if (link.length < 1) {
        return document.getElementById('info').innerHTML = "<p class='error'>Введите ссылку</p>";
    }
    else if (!validLink(link)) {
        return document.getElementById('info').innerHTML = "<p class='error'>Ссылка не действительна</p>";
    }
    if (!path){
        return document.getElementById('info').innerHTML = "<p class='error'>Необходимо выбрать файл</p>";
    }
    let res = await eel.start(link, path.textContent)();


    if (res == 'error0') {
        res = "<p class='error'>Файл logins.txt не был найден</p>"
    }
    if (res == 'error1') {
        res = "<p class='error'>Файл logins.txt не содержит логины и пароли</p>"
    }
    document.getElementById('info').innerHTML += res;
}

function getFilePath(param=false) {
    let data = document.querySelector('.modal');
    if(param) {
      data.innerHTML = `<div class="modalData">
    <div class="data">Создайте файл с расширением .txt, который содержит логины и пароли от аккаунтов dot3.gsu.by.
    <br>Пример заполнения файла:
    <br>login1[пробел]password1
    <br>login2[пробел]password2
    <br>
    <button type="submit" onclick="getFilePath()">Ок</button>
    </div>
    </div>`
    }
    else {
       data.innerHTML = ""
        eel.openFile()(r => document.getElementById('info').innerHTML = r)
    }

}

const validLink = link => {
    if (link.match(/(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi)) {
        return true
    }
    return false
}

const destroyer = () => {
    document.getElementById('info').innerHTML = ""
}