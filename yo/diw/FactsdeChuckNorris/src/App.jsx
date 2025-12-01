import { useState } from "react";
import CrearCategoria from './CategoriasChistes';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
function App(){
    const [categoriaSeleccionada, setCategoriaSeleccionada] = useState("");
    const handleCategoria =(categoria)=> {
        setCategoriaSeleccionada(categoria);
        console.log("Categoria seleccionada:",categoria);
    };

    return (
        <div className="container mt-4">
            <h1 className="mb-3"> s
                <ca
            </h1>
        </div>
    );

}

export default App