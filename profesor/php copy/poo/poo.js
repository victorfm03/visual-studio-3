
let a={nombre: 'Pepe',edad:7, anterior: ()=> this.edad-1};

a.nombre='jose';
a.apellidos='remos';
a.siguiente=()=> this.edad+1;

console.log(a.siguiente)