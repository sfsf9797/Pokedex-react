import { createMuiTheme, TextField, ThemeProvider } from "@material-ui/core";
import React from "react";
import "./Header.css";
import { debounce } from "lodash";

const Header = ({
  setNameOrId,
  nameOrId,
  pokemon,
  setPokemon,
  LightTheme,
}) => {
  const darkTheme = createMuiTheme({
    palette: {
      primary: {
        main: LightTheme ? "#000" : "#fff",
      },
      type: LightTheme ? "light" : "dark",
    },
  });



    const handleText = debounce((text) => {
      setNameOrId(text);
  }, 500);

  return (
    <div className="header">
      <span className="title">{pokemon && nameOrId !=="" ? pokemon.name : "Pokedex"}</span>
      <div className="inputs">
        <ThemeProvider theme={darkTheme}>
          <TextField
            className="search"
            id="filled-basic"
            label="Search by Id or Name"
            onChange={(e) => handleText(e.target.value)}
          />
     
        </ThemeProvider>
      </div>
    </div>
  );
};

export default Header;