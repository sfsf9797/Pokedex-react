import requests
from cache import name2Id, Id2Json
from pokemon import pokemon


class API():

    def __init__(self):
        self.baseUrl = 'https://pokeapi.co/api/v2/pokemon/'
        self.name2Id = name2Id()
        self.Id2Json = Id2Json()


    def call_api(self, url): 
        """
        send a get request to the api 

        Args:
            url (str): the web address 

        Returns:
            dict: a json response from api
        """          
        try:
            response = requests.get(url)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except:
            pass
        else:
            return response.json() 


    def getData(self, idorName):
        """
        get the data from api endpoint if it is not exist in the cache
        and save the data in the cache.

        return the data if it is in the cache

        Args:
            idorName (str]): id or name of pokemon

        Returns:
            dict: pokemon's details
        """        
        data = None
        try:
            #check if idorname is id or name
            if not idorName.isdecimal():
                id = self.name2Id.get(idorName)
            else:
                id = idorName
            data = self.Id2Json.get(id)
        except Exception as e:
            pass

        #if data not in cache
        if not data:
            try:
                url = self.baseUrl + str(idorName)
                data = self.call_api(url)
                locData = self.call_api(data['location_area_encounters'])
                
                pokemonInfo = pokemon(data,locData)

                data = pokemonInfo.getData()

                self.Id2Json.save(data)
                self.name2Id.save(data)
                    
            except:
                pass 

        return data


 