def fillFunc(data: list) -> str:  # takes data and concatenates list contains questions and answers, this list
    # converts to str
    funcJS = """function autoSolve (){
    let data = """ + str(data) + """
        const collection = document.getElementsByClassName("formulation clearfix")
        for (let i = 0; i < collection.length; i++) {
            const question = collection[i].children[2].textContent
            const answers = collection[i].children[3].children[1].children;
            if(data.includes(question)){
                for (let i = 0; i < answers.length; i++) {
                    const selector = answers[i].children[0]
                    const answer = answers[i].children[1]
                    if (`+++${answer.textContent}` == data[data.indexOf(question) + 1]){
                         selector.checked = true;
                        console.log(question)
                        console.log(document.querySelector(`label[for="${answers[i].children[1].htmlFor}"]`))
                    }   
                }
            } else {
                console.log('Error: question not found')
            }                 	
        }
}
autoSolve ();"""
    return funcJS
