import React from "react";
import "./PokeCard.css";

const PokeCard = ({ pokemon, nameOrId, LightTheme, category }) => {
  return (
    <div className="meanings">
   
      {nameOrId === "" ? (
        <span className="subTitle">Start by typing a pokeom id or name in search</span>
      ) : (
        pokemon === null ? (
        <span className="subTitle">Pokemon's name or id not found</span>
        ) : (
          
          <div
                className="singleMean"
                style={{
                  backgroundColor: LightTheme ? "#3b5360" : "white",
                  color: LightTheme ? "white" : "black",
                }}
              >
                 <h2>Stat</h2>
                <hr style={{ backgroundColor: "black", width: "100%" }} />
                <span>
                    <b>Id :</b> {pokemon.id}
                  </span>
                  <span>
                    <b>attack :</b> {pokemon.attack}
                  </span>
                  <span>
                    <b>defense :</b> {pokemon.defense}
                  </span>
                  <span>
                    <b>hp :</b> {pokemon.hp}
                  </span>
                  <span>
                    <b>speed :</b> {pokemon.speed}
                  </span>
                  <span>
                    <b>Type :</b> {pokemon.types && pokemon.types.map(type =><div style={{paddingLeft:'3vw'}}>{type}</div>)}
                  </span>

                  <h2>Location</h2>
                  <hr style={{ backgroundColor: "black", width: "100%" }} />               
                  {pokemon.location && ( (pokemon.location.map(loc => 
                      (<div>
                          <span style={{padding:'5px'}}>
                            <b>location name :</b> {loc.location_name}
                          </span>
                          <span>
                            <b>method :</b> {loc.method}
                          </span>
                        </div>)
                   )))}        
          </div>
        
        )
      )}
    </div>
  );
};

export default PokeCard;