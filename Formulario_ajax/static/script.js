document.getElementById('userForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        nombre: document.getElementById('nombre').value,
        email: document.getElementById('email').value
    };

    fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => Promise.reject(err));
        }
        return response.json();
    })
    .then(data => {
        // Agregar nueva fila a la tabla
        const tbody = document.getElementById('userTable');
        const newRow = `
            <tr>
                <td>${data.id}</td>
                <td>${data.nombre}</td>
                <td>${data.email}</td>
            </tr>
        `;
        tbody.insertAdjacentHTML('beforeend', newRow);
        
        // Limpiar formulario
        document.getElementById('userForm').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert(error.error || 'Ocurrió un error al agregar el usuario');
    });
});