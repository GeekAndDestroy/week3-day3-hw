import requests

class Pokemon:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} is {self.height} tall and weighs {self.weight}."
    
class Berry:
    def __init__(self, name, firmness, flavor):
        self.name = name
        self.firmness = firmness
        self.flavor = flavor


    def __str__(self):
        return f"{self.name} is a {self.firmness} and {self.flavor} fruit."


class PokemonAPI:

    base_url = 'https://pokeapi.co/api/v2/'

    def __init__(self):
        pass
        

    def __get(self, endpoint, name):
        request_url = f"{self.base_url}{endpoint}/{name}/"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        
    def get_pokemon(self, name):
        poke_data = self.__get('pokemon', name)
        if poke_data:
            height = poke_data['height']
            weight = poke_data['weight']
            poke_obj = Pokemon(name, height, weight)
            return poke_obj
        else:
            print('No data for ', name)


    def get_berry(self, name):
        berry_data = self.__get('berry', name)
        if berry_data:
            firmness = berry_data['firmness']['name']
            flavor = berry_data['flavors'][0]['flavor']['name']
            berry_obj = Berry(name, firmness, flavor)
            return berry_obj
        else:
            print('No data for ', name)
            
        
  