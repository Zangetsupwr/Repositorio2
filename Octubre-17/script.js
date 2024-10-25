function handleClick(elemento) {
    console.log(elemento);
    elemento.style.backgroundColor = "red";
}

function handleMouseOver(elemento) {
    console.log(elemento);
    //Cuando mi mouse esta dentro del evento creo un evento que permite escuchar el movimiento del mouse
    let scale = 1;
    elemento.addEventListener('wheel',(e) =>{
        console.log(e);
        console.log(e.wheelDelta);
        //Cambiar el tamaño del elemento

        if (e.wheelDelta < 0){
            scale -=0.1;
            elemento.style.transform =`scale(${scale})`;
        }
        else(e.wheelDelta > 0){
            scale +=0.1;
            elemento.style.transform =`scale(${scale})`;
        }
    }  
)}
