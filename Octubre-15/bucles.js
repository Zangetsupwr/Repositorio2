/*bucle por cantidad finita de veces*/

for(let iterador=0; iterador <10; iterador ++){
    console.log(iterador);
}

/* BUCLE POR CANTIDAD INDEFINIDA DE VECES*/
let aleatorio =0;
while(aleatorio <5){
    aleatorio = Math.random()*10;
    console.log(aleatorio);
}

/* BUCLES Y ARREGLOS */

let arteMarciales = ['Karate', 'Kung Fu', 'Judo', 'Taekwondo', 'Boxeo', 'Muay Thai', 'Jiu Jitsu', 'Aikido', 'Capoeira', 'Krav Maga'];

for(let i=0; i< artesMarciales.length; i++){
    console.log(artesMarciales[i]);
}

//Modernos
artesMarciales.foreach(artesMarciales => {
   console.log(arteMarciales);
});

