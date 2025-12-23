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