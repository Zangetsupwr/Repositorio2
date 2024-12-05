
const host = 'https://swapi.dev/api/'

const endpoint = 'people/1/'


const requestOptions = {
    method: "GET",
    redirect: "follow"
};


const getPerson = async (e) => {
    //PARA EVITAR QUE SE RECARGUE LA PAGINA AL HACER CLICK
    e.preventDefault();
    // Creamos un objeto FormData para obtener el valor del input
    const formData = new FormData(e.target);
    // Obtenemos el valor del input con el name 'id'
    const id = formData.get('id');

    const response = await fetch(`https://swapi.dev/api/people/${id}/`, requestOptions);
    const data = await response.json();
    const personCard = document.getElementById('personInfo');
    console.log(personCard);
    personCard.innerHTML = `
        <h2>Nombre:${data.name}</h2>
        <h3>Altura:${data.height}</h3>
        <h3>Peso:${data.mass}</h3>
        <h3>Color de cabello:${data.hair_color} </h3>
        <h3>Color de piel:${data.skin_color}</h3>
    `;
}


const login = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        body: formData,
        redirect: 'follow'
    });
    const data = await response.json();
    if (data.errors) {
        if (data.errors.password) {
            const errorPassword = document.getElementById('errorPassword');
            errorPassword.innerHTML = data.errors.password;
            errorPassword.setAttribute('type', '');
        }
    } else {
        const errorPassword = document.getElementById('errorPassword');
        errorPassword.innerHTML = "";
        errorPassword.setAttribute('type', 'hidden');
    }
}