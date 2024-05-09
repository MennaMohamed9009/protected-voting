let radio1  = document.querySelector(".a1");
let radio2  = document.querySelector(".a2");
let radio3  = document.querySelector(".a3");
let radio4  = document.querySelector(".a4");
let confirm = document.getElementById("create");
let radio   = document.getElementsByName("a") ;

function addToStorage(boxArr){
    let storage = localStorage.setItem("box",JSON.stringify(boxArr));
    return storage;
}
function getToStorage(){
    let storage = localStorage.getItem("box") === null ? [] : JSON.parse(localStorage.getItem("box"));
    return storage;
}
window.onload = function(){
for(let i =0; i < radio.length ; i++){
    if(getToStorage().indexOf(radio[i].value) !== -1 ) {
        radio[i].checked=true;
        }
    }
}
function removeAll(){
    localStorage.clear();
}
// removeAll();
var checkedRadioValue="";
confirm.onclick = function (e){
    e.preventDefault();
if(radio1.checked) {
    checkedRadioValue= radio1.value;
} 
else if(radio2.checked) {
    checkedRadioValue= radio2.value;
}else if(radio3.checked){
    checkedRadioValue = radio3.value;
}else if(radio4.checked){
    checkedRadioValue = radio4.value;
}
addToStorage(checkedRadioValue)
window.location.href = "{% static 'templates/pages/sendMassege.html'%}"
};



///////////