import { useEffect, useState } from "react";

function CrearCategoria({handler}) {
  const [isLoading, setIsLoading] = useState(true);
  const [categorias, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");

  useEffect(() => {
    async function fetchCategories() {
      try {
        let res = await fetch("https://api.chucknorris.io/jokes/categories");
        let array_category = await res.json();
        setCategories(array_category);
        setIsLoading(false);

        if (array_category.length > 0) {
          setSelectedCategory(array_category[0]);
          handler(array_category[0]);
        }
      } catch (e) {
        alert("Error: ", e);
      }
    }

    if (isLoading) {
      fetchCategories();
    }
  }, [isLoading]);

  return (
    <>
      {categorias}
      <select
        name="categorias"
        value={selectedCategory}
        onChange={(e) => {
          const value = e.target.value;
          setSelectedCategory(value);
          handler(value);
        }}
      >
        {categorias.map((item) => (
          <option key={item} value={item}>
            {item}
          </option>
        ))}
      </select>
    </>
  );
}

export default CrearCategoria;
