/*Al hacer click en comprar el boton desaparece*/
function comprarProducto(boton) {
    boton.target.style.display = "none";
}
/*Al pasar el cursor sobre enviar flores se cambia a enviar bouquets*/
function enviarFlores(boton) {
    boton.target.innerHTML = "Enviar Bouquets";
}
/*Al hacer click en inciar sesion se despliega un mensaje*/
function iniciSesion(event){
    alert("Bienvenido a la tienda FlorManía");
}