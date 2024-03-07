from wrapper import PokemonAPI

def main():
    item = PokemonAPI()
    while True:
        query = input("What would you like info on? pokemon/berry/quit ").lower()
        if query == 'pokemon':
            prompt = input("What Pokemon would you like info on? ").lower()
            poke_obj = item.get_pokemon(prompt)
            print(poke_obj)
        elif query == 'berry':
            prompt = input("What Berry would you like info on? ").lower()
            berry_obj = item.get_berry(prompt)
            print(berry_obj)
        elif  query == 'quit':
            print("Thank you. Come back if you ever need more info!")
            break
        else:
            print("Invalid response. Please ")

main()