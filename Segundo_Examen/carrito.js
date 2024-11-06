
function actualizarCarrito() {
const carritoElemento = document.getElementById('carrito');
carritoElemento.innerHTML = 'carrito.html'; 
carrito.forEach(producto => {
    const item = document.createElement('li');
    item.textContent = `${producto.nombre} - $${producto.precio}`;
    carritoElemento.appendChild(item);
});
}
