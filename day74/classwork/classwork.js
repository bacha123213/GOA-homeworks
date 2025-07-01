let btn = document.getElementById('btn1');

btn.addEventListener('click', function(event) {
    console.log(event);

    document.body.style.backgroundColor = 'black';

    document.body.style.color = 'white';
})