/*Funcion representa cuando se apreta el botón cerrar sesion se abre una alerta con un mensaje*/ 
function BtncerrarSession(){
    alert("Tu sesion de ha cerrado correctamente.");
}
/*Funcion en el momento de hacer clic en un botón de categorias se cambia a otro color */
    function BtncambiarColor(boton) {
        boton.style.backgroundColor = "#5d1636";
    }

    /*Funcion para el incremento de Me Gusta (Likes como en las redes sociales)*/
    function darLike(id){
        const likeCountElement = document.getElementById(id);
        let currentLikes = parseInt(likeCountElement.textContent);
        currentLikes++;
        likeCountElement.textContent = `${currentLikes} like(s)`;
    }
    