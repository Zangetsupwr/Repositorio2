/*cuando el usuario haga click en login , muestra una alerta con la bienvenida al texto que se ingresó*/
document.getElementById('loginBtn').addEventListener('click', function () {
    var username = document.getElementById('username').value;
    alert('Bienvenido, ' + username + '!');
});

/* Al pasar el mouse sobre la imagen esta cambia a otra imagen*/

document.getElementById("imagen").addEventListener("mouseover", function() {
    this.src = "comida-mexicana2.jpg";
});

document.getElementById("imagen").addEventListener("mouseout", function() {
    this.src = "comida-mexicana.jpg";
});

/* Contar los pedidos*/
function aumentarCarrito() {
    const carrito = document.getElementById("carritoCantidad");
    let cantidadActual = parseInt(carrito.textContent);
    cantidadActual++;
    carrito.textContent = `${cantidadActual}`;
}