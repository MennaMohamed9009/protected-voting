let email = document.querySelector(".email input") 
let password = document.querySelector(".password input") 
let loginBtn2 = document.querySelector(".create") 

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
// removeAll();
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

loginBtn2.addEventListener('click',(e) => {
    e.preventDefault();
let id  = Date.now();
let  user = new User(id,email.value , password.value);

if (email.value !== "") {
    userArr=[...userArr,user]
    addToStorage(userArr);
    email.value ='';
    password.value ='';
    window.location.href="{% static 'templates/pages/login.html'%}"
}

else{
    return false ;
}

}


);