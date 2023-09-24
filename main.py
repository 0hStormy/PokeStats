# main.py

# Packages
import json
import os
import time
from Termicolor import Color

# Stat Printer
def read_stats():
    print("Name: " + PokemonName + "\n")
    print(Color("1. HP: ", PokemonHP).red)
    print(Color("2. Attack: ", PokemonAttack).yellow)
    print(Color("3. Defense: ", PokemonDefense).green)
    print(Color("4. Special Attack: ", PokemonSpAtk).cyan)
    print(Color("5. Special Defense: ", PokemonSpDef).blue)
    print(Color("6. Speed: ", PokemonSpeed).magenta)
    print("7. Total: ", StatTotal)

# Clears Screen
os.system("clear")

# Get and read JSON file
fileloc = input("Where is the json file? ")

# Checks if file exists
if os.path.isfile(fileloc) == True:
    
    # Open and read file
    with open(fileloc) as f:
        tempjson = f.read()
        jsoninfo = json.loads(tempjson)

        # Declare Variables
        PokemonName = (jsoninfo["Name"])
        PokemonHP = (jsoninfo["HP"])
        PokemonAttack = (jsoninfo["Attack"])
        PokemonDefense = (jsoninfo["Defense"])
        PokemonSpAtk = (jsoninfo["SpAtk"])
        PokemonSpDef = (jsoninfo["SpDef"])
        PokemonSpeed = (jsoninfo["Speed"])
        StatTotal = (jsoninfo["Total"])
        
        # Clears Screen
        os.system("clear")

        # Reads Stats
        read_stats()

# If file does not exist
else:
    print("File does not exist")
    time.sleep(2)