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

    document.getElementById('info').innerHTML += res;
}

function getFilePath(param=false) {
    let data = document.querySelector('.modal');
    if(param) {
      data.innerHTML = `
    <div class="modalData">
        <div class="modalWindow">
            <div class="modalMainText">Создайте файл с расширением .txt, который содержит логины и пароли от аккаунтов dot3.gsu.by.</div>
            <div class="modalExample">
                Пример заполнения файла: <br>
                <br>login1[пробел]password1
                <br>login2[пробел]password2
                <br>
            </div>
        <button type="submit" onclick="getFilePath()" class="modalSubmitBtn">Ок</button>
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

async function deleteDub(){
    let filePath = document.getElementById('filePathTag').textContent
    let result = await eel.deleteDub(filePath)
    document.getElementById('submitDelete').remove()
}

const destroyer = () => {
    document.getElementById('info').innerHTML = ""
}