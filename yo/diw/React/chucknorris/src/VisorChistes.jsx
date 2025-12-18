import { useState,useEffect } from "react";
import CrearCategoria from "./CategoriasChistes";

function VisorChistes(){

    const [textoChiste,setTextoChiste]=useState('');
    const [selectedCategory,setselectedCategory]=useState('');
    const [error,setError]=useState(null);

    const [isLoading,setIsLoading]=useState(true);

    function handleChange(categoria){
        setselectedCategory(categoria);
        setIsLoading(true);
    }

    useEffect(() =>{

        async function fetchChiste() {
            
            try{

                let response=await fetch(`https://api.chucknorris.io/jokes/random?category=${selectedCategory}`);

                let chiste=await response.json();

                setTextoChiste(chiste.value);
                setError(null);

            }catch(e){
                setError("No se pudo recuperar el chiste: "+e)
            }
            setIsLoading(false);

        }

        if (isLoading && selectedCategory!=""){
            fetchChiste();
        }
    },[isLoading,selectedCategory]
)

return(
    <>

        <h1>chistes de chuck norris</h1>
        <CrearCategoria handler={handleChange}/>
        
        {
            isLoading ? <p>Cargando.....</p>: <p>{textoChiste}</p>
        }
        {
            error!=null?<p>{error}</p>:""
        }
        <button onClick={()=> setIsLoading(true)}>otro chiste</button>
    
    </>
)
    
}

export default VisorChistes;