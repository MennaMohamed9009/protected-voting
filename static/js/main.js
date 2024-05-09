let menuBtn = document.querySelector(".menu")
let  ulMenu = document.querySelector(".header ul")
let  menuAfter = document.querySelector(".header ul")
let link =document.querySelector(".half2 a");

menuBtn.onclick = function(){
ulMenu.classList.toggle("active");
menuBtn.classList.toggle("active");
}

if(localStorage.getItem("user") === null){
link.href="{% static 'templates/pages/login.html'%}"
}
else{
    link.href="{% static 'templates/pages/election.html'%}"
}


