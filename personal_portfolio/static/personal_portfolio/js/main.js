

function openModall(mythis) {
    // console.log('src')
    // console.log(document.getElementsByClassName('sert_src')[0].src)

    document.getElementsByClassName('modal-sert')[0].classList.add('modal-show');
    // document.getElementsByClassName('my_body')[0].classList.add('layer');
    document.getElementsByClassName('layer')[0].style.display = 'block';
    document.getElementsByClassName('sert_src')[0].src = mythis.src

    // document.getElementsByClassName('img_modal')[0].src = mythis.src
    // $('#exampleModal').modal('show') // query запуск по id при нажати на фото
    // document.getElementsByClassName('modal-open')[0].style.paddingRight = '0px'
    // // console.log(modal('show'))
    // document.getElementById('exampleModal').style.top = '20%'
    // //document.getElementsByClassName('myModal')[0] = document.getElementsByClassName('my-src')[0].src
    // first_push_image = mythis
}

function closeModal(){
    document.getElementsByClassName('modal-sert')[0].classList.remove('modal-show')
    document.getElementsByClassName('layer')[0].style.display = 'none';
}

window.addEventListener("keydown", function (evt){
    if (evt.keyCode === 27){
        if(document.getElementsByClassName('modal-sert')[0].classList.contains('modal-show')){
            evt.preventDefault();
            document.getElementsByClassName('modal-sert')[0].classList.remove('modal-show')
            document.getElementsByClassName('layer')[0].style.display = 'none';
        }
    }
});