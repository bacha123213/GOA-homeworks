function userName(user)  {
    user.preventdefault();
    let input = document.getElementById("username").value;

    console.log(input.value)

    input.value = "";
}

userName(user)

// შექმენით ფუნქცია სახელად concStrings. ფუნქციაში უნდა გქონდეთ ორი ცვლადი და ორივეში შეინახეთ prompt-ით შემოტანილი ინფორმაცია. საბოლოოდ დაბეჭდეთ ამ ორი ცვლადის კონკატინაციის შედეგი alert box-ში

function concStrings() {
    let a = prompt("Enter 1st word: ")
    let b = prompt("Enter 2nd word: ")
    let result = a + b
    alert("Result of Concatination: ", result)
}

concStrings()