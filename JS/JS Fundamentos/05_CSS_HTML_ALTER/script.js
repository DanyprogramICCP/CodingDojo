var saiyaImg = document.querySelector("#fav-saiya");

console.log(saiyaImg);

function callVegeta(element){
    saiyaImg.src = "vegeta1.png";
    element.style.backgroundColor = "goldenrod";
    element.remove();
   // console.log(saiyaImg.src);
  //  console.log(element);
}

function callGoku(element){
    element.classList.add("btn");
    saiyaImg.src = "goku1.png";
    console.log(element.classList);
   
}

function setActive(element) {
    console.log(element.classList);
    if(element.innerText = "Cambiar al modo oscuro") {
        element.innerText = "Cambiar al modo claro";
       // element.classList.remove("dark-mode");
    } else{
        element.innerText = "Cambiar al modo claro";
    }
    
}
