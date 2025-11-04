"use strict";

// Codificar aquí las clases
class Libro{
    #idlibro;
    #idgenero;
    #autor;
    #decripcion;
    #titulo;
    #imagen;

    constructor(idlibro,idgenero,autor,decripcion,imagen,titulo){
        this.#idlibro=this.#idlibro;
        this.idgenero=idgenero;
        this.autor=autor;
        this.decripcion=decripcion;
        this.imagen=imagen;
        this.titulo=titulo;
    }

    get idlibro(){
        return this.idlibro;
    }

    set idlibro(valor){
        this.idlibro=valor;
    }

    get idgenero(){
        return this.idgenero;
    }

    set idgenero(valor){
        this.idgenero=valor;
    }

    get descripcion(){
        return this.descripcion;
    }

    set descripcion(valor){
        this.descripcion=valor;
    }

    get autor(){
        return this.autor;
    }

    set autor(valor){
        this.autor=valor;
    }

        get titulo(){
        return this.titulo;
    }

    set titulo(valor){
        this.titulo=valor;
    }

        get imagen(){
        return this.imagen;
    }

    set imagen(valor){
        this.imagen=valor;
    }
    


}



class genero{
    #idgenero;
    #genero;


    constructor(idgenero,genero){
        this.#idgenero=this.#idgenero;
        this.idgenero=genero;
    }

    get idgenero(){
        return this.idgenero;
    }

    set idgenero(valor){
        this.idgenero=valor;
    }

    get genero(){
        return this.genero;
    }

    set genero(valor){
        this.genero=valor;
    }
    
 toJSON(){
    
    return

    
 }
    
}