# main.py

# Packages
import json
import os
import time
from Termicolor import Color

# Stat Printer
def read_stats():
    # Open and read file
    with open(fileloc) as f:
        tempjson = f.read()
        jsoninfo = json.loads(tempjson)
    
    # Declare Variables
    PokemonName = (jsoninfo["name"])
    PokemonHP = (jsoninfo["hp"])
    PokemonAttack = (jsoninfo["attack"])
    PokemonDefense = (jsoninfo["defense"])
    PokemonSpAtk = (jsoninfo["spatk"])
    PokemonSpDef = (jsoninfo["spdef"])
    PokemonSpeed = (jsoninfo["speed"])
    StatTotal = (jsoninfo["total"])
    
    # Clears Screen
    os.system("clear")

    # Prints stats
    print("Name: " + PokemonName + "\n")
    print(Color("HP: ", PokemonHP).red)
    print(Color("Attack: ", PokemonAttack).yellow)
    print(Color("Defense: ", PokemonDefense).green)
    print(Color("Secial Attack: ", PokemonSpAtk).cyan)
    print(Color("Special Defense: ", PokemonSpDef).blue)
    print(Color("Speed: ", PokemonSpeed).magenta)
    print("Total: ", StatTotal)
    print()
    return

# Change Stats
def modify_stats():
    statChange = input("Enter new stats: ")
    with open(fileloc) as f:
        jsonStat = json.load(f)
        jsonStat[statInput] = statChange
    
    # Create a temporary file containing the updated JSON data
    tempFile = "temp_{}.json".format(os.getpid())
    with open(tempFile, 'w') as tf:
        json.dump(jsonStat, tf, indent=4)
    
    # Rename the temporary file over the original file
    os.replace(tempFile, fileloc)
    
    read_stats()
    return

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

        # Reads Stats
        read_stats()
        
        working = True
        
        while working == True:
            statInput = input("Stat Name (lowercase only): ")
            modify_stats()
            

# If file does not exist
else:
    print("File does not exist")
    time.sleep(2)