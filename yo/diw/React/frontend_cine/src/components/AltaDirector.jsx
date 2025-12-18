import { useState } from "react";
import { Typography } from "react";

function AltaDirector() {
  const [director, setDirector] = useState({
    id_director: "",
    name: "",
    birth_date: "",
    biography: "",
    potho_url: "",
  });

  const [isCamposValues, setisCamposValues] = useState({
    name: true,
    birth_date: true,
    biography: true,
    potho_url: true,
  });

function handleChange(e){
    setDirector({...director,[e.target.name]:e.target.value})
}

  return (
    <>
      <Typography variant="h3">Alta de director</Typography>

      <Grid container spacing={2}>
        <Grid item size={{ xs: 7 }}>
          <DatePicker label="fecha de nacimiento"></DatePicker>
        </Grid>
      </Grid>
    </>
  );
}

export default AltaDirector;
