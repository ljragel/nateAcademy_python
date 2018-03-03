charmander_health=100
charmander_attacks=("BOLAFUEGO", "SOFOCO")

squirtle_health=120
squirtle_attacks=("HIDROBOMBA","SALPICADURA")

bulvasur_helath=80
bulvasur_attacks=("LATIGOCEPA", "HOJAAFILADA")

pikachu_health=100
pikachu_attacks=("COLAFERREA", "TRUENO")

your_health=-1
your_attacks=()

aux_pokemon_name=""
your_pokemon="PIKACHU"

while your_pokemon=="PIKACHU" and aux_pokemon_name!="":
    your_pokemon = str(input("Introduce el nombre el pokemon(Charmander/Squirtle/Bulvasur)."))
    if (your_pokemon != "CHARMANDER" and your_pokemon != "SQUIRTLE" and your_pokemon != "BULVASUR"):
        print("No tenemos a ningun pokemon con ese nombre, lo siento, introduce un nombre valido: ")






if enemy_name=="CHARMANDER":

    print("Tu: CHARMANDER  te elijo a ti")
    enemy_health=charmander_health
    your_attacks = charmander_attacks
elif enemy_name=="BULVASUR":
    print("Tu: BULVASUR te elijo a ti")
    enemy_health=charmander_health
    your_attacks_attacks=bulvasur_attacks
elif enemy_name=="SQUIRTLE":
    print("Tu: SQUIRTLE te elijo a ti")
    enemy_health=charmander_health
    your_attacks=squirtle_attacks