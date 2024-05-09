let email = document.querySelector(".email input") 
let password = document.querySelector(".password input") 
let loginBtn = document.querySelector(".login-btn #loginBtn") 

let userArr = [];

class User{
    constructor(id,email,password){
        this.id =id
        this.email = email
        this.password = password
    
    }
}

window.addEventListener("keydown", (e) => {
    if (e.keyCode == 13) {
        loginBtn.click();
    }
});
function removeAll(){
    userArr.length =0;
    localStorage.clear();
}

function addToStorage(userArr){
    let storage =localStorage.setItem("user",JSON.stringify(userArr));
    return storage;
}
function getToStorage(){
    let storage = localStorage.getItem("user") === null ? [] : JSON.parse(localStorage.getItem("user"));
    return storage;
}

function removeArray(id){
    userArr = userArr.filter((item) => item.id != +id);
    addToStorage(userArr)
}


userArr = getToStorage();


loginBtn.addEventListener('click',(e) => {
    e.preventDefault();
let id  = Date.now();
let  user = new User(id,email.value , password.value);

if (email.value !== "") {
    userArr=[...userArr,user]
    addToStorage(userArr);
    email.value ='';
    password.value ='';
}
else{
    return false;
}
window.location.href = "{% static 'templates/pages/startElection.html'%}";
});

