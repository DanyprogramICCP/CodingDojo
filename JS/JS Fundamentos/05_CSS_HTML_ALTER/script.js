
    
    function setActive(element) {
        element.classList.add("dark-mode");
    }

    function setActive(element) {
        element.style.backgroundColor = "#222222";
        element.style.color = "#ffffff";
    }
    function setActive(element) {
        if(element.classList.include("dark-mode")) {
            element.innerText = "Cambiar al modo claro";
            element.classList.remove("dark-mode");
        } else {
            element.innerText = "Cambiar al modo oscuro";
            element.classList.add("dark-mode");
        }
    }