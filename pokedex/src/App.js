import { Container, Switch, withStyles } from "@material-ui/core";
import { grey } from "@material-ui/core/colors";
import axios from "axios";
import { useEffect, useState } from "react";
import "./App.css";
import PokeCard from "./components/PokeCard/PokeCard";
import Footer from "./components/Footer/Footer";
import Header from "./components/Header/Header";

function App() {
  const [nameOrId, setNameOrId] = useState("");
  const [pokemon, setPokemon] = useState([]);
  const [LightTheme, setLightTheme] = useState(false);

  const dictionaryApi = async () => {
    try {
      const data = await axios.get(
        `http://localhost:5000/${nameOrId}`
      );
      
      setPokemon(data.data);
    } catch (error) {
      console.log(error);
    }
  };

  console.log(pokemon);

  useEffect(() => {
    dictionaryApi();
    // eslint-disable-next-line
  }, [nameOrId]);

  const PurpleSwitch = withStyles({
    switchBase: {
      color: grey[50],
      "&$checked": {
        color: grey[900],
      },
      "&$checked + $track": {
        backgroundColor: grey[500],
      },
    },
    checked: {},
    track: {},
  })(Switch);

  return (
    <div
      className="App"
      style={{
        height: "100vh",
        backgroundColor: LightTheme ? "#fff" : "#282c34",
        color: LightTheme ? "black" : "white",
        transition: "all 0.5s linear",
      }}
    >
      <Container
        maxWidth="md"
        style={{
          display: "flex",
          flexDirection: "column",
          height: "100vh",
          justifyContent: "space-evenly",
        }}
      >
        <div
          style={{ position: "absolute", top: 0, right: 15, paddingTop: 10 }}
        >
          <span>{LightTheme ? "Dark" : "Light"} Mode</span>
          <PurpleSwitch
            checked={LightTheme}
            onChange={() => setLightTheme(!LightTheme)}
          />
        </div>
        <Header
          setNameOrId={setNameOrId}
          nameOrId={nameOrId}
          pokemon={pokemon}
          setPokemon={setPokemon}
          LightTheme={LightTheme}
        />
        {
          <PokeCard
            pokemon={pokemon}
            nameOrId={nameOrId}
            LightTheme={LightTheme}
          />
        }
      </Container>
      <Footer/>
    </div>
  );
}

export default App;