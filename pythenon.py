import sys
import json
import random
import time

from pokemon import Pokemon

class Pythenon:
    def __init__(self):
        #En konstruktor
        self.playerMadePokemonName = ""
        self.originalPokemonName = ""
        self.wins = 0
        self.losses = 0
        
    def welcome(self):
        #welcomes the player
        print("*"*40)
        print("Välkommen till Pokémon!")
        print("*"*40)
    
    def setPlayerAndPokemonNames(self):
        #sets the player and the pokemons name into the class
        pokemonExists = False

        while pokemonExists == False:

            self.playerMadePokemonName = input("Vad heter din Pokémon? ")
            self.originalPokemonName = input("Vilken pokémon är det? ")

            with open('pokemons.json') as f:
                data = json.load(f)
            
            for i in data:
                if self.originalPokemonName == i:
                    #found the pokemon
                    pokemonExists = True

            if pokemonExists == True:
                Pythenon.menu(self)
            else:
                print("Den pokémon du försöker välja finns inte, välj någon av följande:")

                for i in data:
                    print(f"-{i}")
                    pokemonExists = False
                
    def menu(self):
        #main of the game player chooses what to do
        gameIsPlaying = True

        while gameIsPlaying == True:
            print("1) Duellera\n2) Byt pokémon\n3) Se statistik\n0: Avsluta")

            val = str(input("Ange val: "))
            
            match val:
                case '1': 
                    #print("Fight some pokemon")
                    Pythenon.createPokemonObjects(self)
                case '2':
                    #print("Byta en pokemon")
                    Pythenon.setPlayerAndPokemonNames(self)
                case '3':
                    #see the wins and losses
                    Pythenon.statistics(self)
                case '0':
                    print("Avslutar spelet")
                    gameIsPlaying = False
                    sys.exit()
                case '_':
                    print("No comprende")
    
    def createPokemonObjects(self):
        #print("Skapar objekt av spelarens och datorns pokemon")

        with open('pokemons.json') as f:
            data = json.load(f)
        
        #self.playerMadePokemonName = "Mr Asda"
        #self.originalPokemonName = "Dwane 2"
        selectedPokemonName = self.originalPokemonName


        pokemonType = data[selectedPokemonName]["type"]
        pokemonDamage = data[selectedPokemonName]["damage"]
        pokemonHp = data[selectedPokemonName]["hp"]
        pokemonWeakness = data[selectedPokemonName]["weakness"]

        playerPokemon = Pokemon(selectedPokemonName,pokemonType,pokemonDamage,pokemonHp,pokemonWeakness)
        #print(playerPokemon.__str__())

        computermonName = random.choice(list(data))
        computermonType = data[computermonName]["type"]
        computermonDamage = data[computermonName]["damage"]
        computermonHp = data[computermonName]["hp"]

        computermonHpDouble = computermonHp * 1.5
        computermonHpHalved = computermonHp * 0.5
        computermonHp = int(random.uniform(computermonHpHalved, computermonHpDouble))
        
        computermonWeakness = data[computermonName]["weakness"]

        computerPokemon = Pokemon(computermonName,computermonType,computermonDamage,computermonHp,computermonWeakness)
        #print(computerPokemon.__str__())
        Pythenon.pokemonFight(self, playerPokemon, computerPokemon)
        
    def pokemonFight(self, playerPokemon, computerPokemon):
        #print("Din pokemon och datorns pokemon slåss här")

        print("Duell mellan:")

        playerHealthPoints = playerPokemon.getHp()
        playerAttackPoints = playerPokemon.getDamage()
        print(f"- Du: {self.playerMadePokemonName}({self.originalPokemonName}), HP: {playerHealthPoints} , Attack: {playerAttackPoints} ")
        
        computermonName = computerPokemon.getName()
        computermonHealthPoints = computerPokemon.getHp()
        computermonAttackPoints = computerPokemon.getDamage()
        print(f"- Dator {computermonName}, HP: {computermonHealthPoints} , Attack {computermonAttackPoints}")

        fightGoingOn = True

        print("*"*40)
        print("- Datorn börjar")
        print("*"*40)

        playerType = playerPokemon.getType()
        computerType = computerPokemon.getType()

        playerPokemon.determineIfWeaknessIsSameAsStrength(computerType)
        computerPokemon.determineIfWeaknessIsSameAsStrength(playerType)

        playerHealthPoints = playerPokemon.getHp()
        computermonHealthPoints = computerPokemon.getHp()
        print(f"Du {playerHealthPoints}hp, Datorn {computermonHealthPoints}hp")
        print("*"*40)

        while fightGoingOn == True:
            #Fight happens here

            #COMPUTER ATTACK STARTS HERE
            computerAttackDamage = computerPokemon.attack()
            #print(f"Thing attacked you for {computerAttackDamage} ")
            playerPokemon.setHpAfterAttack(computerAttackDamage)

            print(f"{computermonName} attackerar: {computerAttackDamage}")

            playerHealthPoints = playerPokemon.getHp()
            computermonHealthPoints = computerPokemon.getHp()

            if playerHealthPoints >= 0:
                print(f"Du {playerHealthPoints}hp, Datorn {computermonHealthPoints}hp")
                print("*"*40)

            if playerPokemon.isAlive() == False:
                print(f"Vinnare är datorn: {computermonName}")
                fightGoingOn = False
                self.losses = self.losses+1

                Pythenon.menu(self)

            if computerPokemon.isAlive() == False:
                print(f"Vinnare är {self.playerMadePokemonName}({self.originalPokemonName})!!\nGrattis på vinsten!")
                fightGoingOn = False
                self.wins = self.wins+1

                Pythenon.menu(self)

            time.sleep(0.5)
            #PLAYER ATTACK STARST HERE

            playerAttackDamage = playerPokemon.attack()
            #print(f"You attacked thing for {playerAttackDamage} ")
            computerPokemon.setHpAfterAttack(playerAttackDamage)

            print(f"{self.playerMadePokemonName} ({self.originalPokemonName}) attackerar: {playerAttackDamage}")
            playerHealthPoints = playerPokemon.getHp()
            computermonHealthPoints = computerPokemon.getHp()
            if computermonHealthPoints >= 0:
                print(f"Du {playerHealthPoints}hp, Datorn {computermonHealthPoints}hp")
                print("*"*40)

            if playerPokemon.isAlive() == False:
                print(f"Vinnare är datorn: {computermonName}")
                fightGoingOn = False
                self.losses = self.losses+1

                Pythenon.menu(self)

            if computerPokemon.isAlive() == False:
                print(f"Vinnare är {self.playerMadePokemonName}({self.originalPokemonName})!!\nGrattis på vinsten!")
                fightGoingOn = False
                self.wins = self.wins+1 

                Pythenon.menu(self)
            
            time.sleep(0.5)
            
    def statistics(self):
        print("="*40)
        print(f"Du har vunnit {self.wins} gånger och förlorat {self.losses} gånger")
        print("="*40)
