# main.py

# Packages
import json
import os
import time

# Stat Printer
def read_stats():
    print("Name: " + PokemonName + "\n")
    print("HP: ", PokemonHP)
    print("Attack: ", PokemonAttack)
    print("Defense: ", PokemonDefense)
    print("Special Attack: ", PokemonSpAtk)
    print("Special Defense: ", PokemonSpDef)
    print("Speed: ", PokemonSpeed)
    print("Total: ", StatTotal)

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