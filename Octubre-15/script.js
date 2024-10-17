/*Variables*/
var nombre = "Peter"; //global , se puede acceder desde cualquier parte del codigo
let apellido="Parker"; //Local, solo se puede acceder dentro del scope donde se declaró
const edad=18; //

//Primitivos
let string ="Hola mundo";
let number = 18 ;
let nullValue = null;
let underfinedValue=undefined;

//compuestos

let array =[1,2,3];
let object={key: "value"};
let gruposDeBandas =["Grupo Firme","Banda MS","Banda el recorrido"];


//Anidados 
let nestedArray = [1,[2,3]];//Arreglo anidado
let nestedObject ={key:{key:"value"}};//Objeto anidado
let mixed = [1,{key:"value"}];//Arreglo con objeto anidado




//Condicionales
edad =18;
if (edad >=18){
    console.log("puede comprar licor");
}else{
        console.log("No puede comprar licor");
    }


if(edad >=21){
    console.log("Puedes votar en las elecciones presidenciales");
}else if(edad >=18){
    console.log("puede votar en las elecciones municipales");

}else{
    console.log("No puede votar");
}

/*OPERADOR DE COMPARACION*/
1 >2 //TRUE
1 <2 // FALSE
1>=2 //FALSE
1<=2 // TRUE
1==2 // FALSE
1 === 2 //FALSO //COMPARACION DE VALORES Y TIPOS DE DATOS