from flask import Flask
from flask import request
from flask import jsonify 
from pokeApi import api 
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

PokemonApi = api.API()

@app.route('/<nameOrId>')
@cross_origin()
def pokemonAPI(nameOrId):
    data = PokemonApi.getData(nameOrId)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')