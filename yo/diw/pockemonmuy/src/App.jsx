import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import { useEffect, useState } from "react";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import { justifyContent } from "@mui/system";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Pokecard from "./Pokecard";

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [arrayDatos, setArrayDatos] = useState(null);
  const [pokemonId, setPokemonId] = useState("");
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchPokemon() {
      try {
        let response = await fetch(
          `https://pokeapi.co/api/v2/pkemon/${pokemonId}`
        );

        if (response.ok) {
          let datosPokemon = await response.json();
          setArrayDatos(datosPokemon);
          setError(null);
        }else if(response.status==404){
          setError("El pokemon no existe");
          setArrayDatos(null);
        }else{
          setError("error");
          setArrayDatos(null);
        }
      } catch (e) {
        setError("No se conecto al servidor");
      }
      setIsLoading(false);
    }
    if (isLoading){
      fetchPokemon();
    }
  },[isLoading]);

  return (
    <>
      <Grid container>
        <Grid
          size={{ xs: 12, md: 6, lg: 4 }}
          offset={{ xs: 0, md: 3, lg: 4 }}
          sx={{
            mt: 2,
          }}
        >
          <Stack
            direction="column"
            sx={{
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <Typography variant="h5" align="center">
              Pokemon Info
            </Typography>

            <TextField
              fullWidth
              variant="outlined"
              label="pokemon id/name"
              name="pokemonID"
              value={pokemonId}
              onChange={(e) => setPokemonId(e.target.value)}
            ></TextField>
            <Button variant="contained">Buscar Pkemon</Button>

            {arrayDatos != null ? (
              <Pokecard pokemon={arrayDatos}></Pokecard>
            ) : (
              <>
                {error != null ? (
                  <Typography variant="h6"> no hay datos</Typography>
                ) : (
                  <Typography variant="h6"> no hay datos</Typography>
                )}
              </>
            )}
          </Stack>
        </Grid>
      </Grid>
    </>
  );
}

export default App;
