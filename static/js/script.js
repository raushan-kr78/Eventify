
const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const text = document.querySelector('.short-desc')


let index = 0;

function showSlide(i) {
    if (i < 0){ index = images.length - 1;
    }
    else if (i >= images.length) {index = 0;
    }
    else index = i;

    slides.style.transform = `translateX(${-index * 100}%)`;
}


nextBtn.addEventListener('click', () => showSlide(index + 1));
prevBtn.addEventListener('click', () => showSlide(index - 1));


// setInterval(() => showSlide(index + 1), 3000);
window.addEventListener('scroll', function() {
    const header = document.getElementById('main-header');
    if (window.scrollY > 670) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
const profile =document.querySelector('.profile');
let clicked = false;
profile.addEventListener('click',function(){
    const dorpDown = document.getElementById('drop-down');
    if(clicked==false){
        dorpDown.classList.add('drop-down-show');
        console.log(clicked);
        
        
        clicked=true;
    }else{
        dorpDown.classList.remove('drop-down-show');
        clicked=false
        console.log(clicked);
        
    }
})
