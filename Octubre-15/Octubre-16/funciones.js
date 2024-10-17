const persona1 = {
    rut: "1234567-8",
    nombre: "Franco",
    apellido: "Armani",
    cuentaBancaria: {
        banco: "Banco de Chile",
        tipoCuenta: "Cuenta Corriente",
        saldo: 1000
    }
}

const persona2 = {
    rut: "8765432-1",
    nombre: "John",
    apellido: "Cordoba",
    cuentaBancaria: {
        banco: "Banco Itau",
        tipoCuenta: "Cuenta Corriente",
        saldo: 500
    }
}

const persona3 = {
    rut: "1928375-6",
    nombre: "Martin",
    apellido: "Palermo",
    cuentaBancaria: {
        banco: "Banco Santander",
        tipoCuenta: "Cuenta Corriente",
        saldo: 2000
    }
}

console.log(persona1.cuentaBancaria.saldo);
console.log(persona1.cuentaBancaria.saldo = 2000);

/*TRANSACCION DE DINERO*/
function depositar(persona,monto){
    persona.cuentaBancaria.saldo += monto;
}

function verSaldo(perosna){
    console.log(persona.cuentaBancaria.saldo);
}

//Funciones procedimentales
// Son funciones que no retornan un valor
function saludar(){
    console.log("hola");
}

function saludarPersona(nombre){
    console.log("Hola" +nombre);
}

function obtenerFecha(){
    return new Date();
}

console.log(obtenerFecha());


const numerosRandom=[1,62,635,64,98,13,7,22];
function duplicarNumneros(numero){
    console.log(numero*2);
}
numerosRandom.forEach(duplicarNumneros);

//funcion anonima

numerosRandom.forEach(function(numero){
    console.log(numero*2);
});

numerosRandom.forEach((numeros)=>{
console.log(numero*2);
});