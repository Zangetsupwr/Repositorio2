/*Al aprrtar el boton rentar se cambia de color rojo y se cambia a no disponible*/
    function marcarComoNoDisponible(event) {
        const button = event.target;
        if (!button.classList.contains('no-disponible')) {
            button.classList.add('no-disponible');
            button.textContent = 'No disponible';
            button.style.backgroundColor = 'red';
        }
    }
const botones = document.querySelectorAll('.rentarBtn');
botones.forEach(button => {
    button.addEventListener('click', marcarComoNoDisponible);
});

function incioSesion(){
    alert('Inicio de sesion exitoso !');
}

/*Al hacer click en los generos el titulo debe cambiar al genero elegido*/
function cambiarTitulo(genero) {
    document.getElementById('texto').innerText ="\nLibros de " + genero;
}