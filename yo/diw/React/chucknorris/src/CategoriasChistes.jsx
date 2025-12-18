import { useState,useEffect } from "react";

function CrearCategoria({handler}){

    const [isLoading, setIsLoading]=useState(true);

    const [categories, setCategories]=useState([]);

    const [error, setError] = useState(null);
    const [categoriaSeleccionada, setCategoriaSeleccionada] = useState("");

    useEffect(() => {
        async function fetchCategorias() {
            
            try{

                let response= await fetch("https://api.chucknorris.io/jokes/categories");

                let arrayCategorias=await response.json();

                setCategories(arrayCategorias);

                if (arrayCategorias.length>0){
                    setCategoriaSeleccionada(arrayCategorias[0]);
                    handler(arrayCategorias[0])
                }

                setIsLoading(false);
                setError(null)

            }catch(e){
                setError("No se pudo recuperar la informacion: "+e)
            }
            setIsLoading(false)
        }
        if(isLoading){
                fetchCategorias();
            }
    },[isLoading])

    if(error!=null){
        return(
             <>
                <h1>{error}</h1>
                <button onClick={()=> setIsLoading(true)}>reintentar</button>
            </>
        )
    }else{
    return(
        
        <>
        {isLoading?(
            <div>
                <h1>Cargando......</h1>
            </div>
        ):(
            <select name="categorias" value={categoriaSeleccionada} onChange={(evento) =>{
                setCategoriaSeleccionada(evento.target.value);
                handler(evento.target.value);
            }}>

            {categories.map((item)=>(
                <option key={item} value={item}>{item}</option>
            )
            )
            }
            </select>
        )}
        </>
    )

}
}

export default CrearCategoria;