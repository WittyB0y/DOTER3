eel.expose(writer);
function writer(data) {
    document.getElementById('info').innerHTML += data;
    document.getElementById('info').scrollTop = document.getElementById('info').scrollHeight
}
eel.expose(readSavedFileName)
async function readSavedFileName() {
    let file = document.getElementById('uniSavedFile').textContent;
    await showerPushNot()
}

async function getLink() {
    let link = document.getElementById('link').value;
    let path = document.getElementById('pathToFile');
    destroyer()

    if (link.length < 1) {
        return document.getElementById('info').innerHTML = "<div class='notification error'>Введите ссылку</div>";
    }
    else if (!validLink(link)) {
        return document.getElementById('info').innerHTML = "<div class='notification error'>Ссылка не действительна</div>";
    }
    if (!path){
        return document.getElementById('info').innerHTML = "<div class='notification error'>Необходимо выбрать файл</div>";
    }
    let res = await eel.start(link, path.textContent)();
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

function showerPushNot() {
    const divWindowResult = document.getElementById('idwindow')
    divWindowResult.style.display = "flex"
    setInterval(()=>{
        divWindowResult.style.display = "none"
    }, 2100)
}