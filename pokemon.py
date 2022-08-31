import random

class Pokemon:
    def __init__(self,name,type,damage,hp,weakness):
        #initialiser for the pokemon class. 
        self.name = name
        self.type = type
        self.damage = damage
        self.hp = hp
        self.weakness = weakness
        self.enemyPokemonStrengthIsThisPokemonsWeakness = False

    def getName(self):
        #returns the name of the pokemon
        return self.name
    
    def getHp(self):
        #returns the hp of the pokemon
        return self.hp

    def getDamage(self):
        ##returns the damage of the pokemon
        return self.damage

    def getType(self):
        ##returns the type of the pokemon
        return self.type
    
    def getWeakness(self):
        #returns the weakness of the pokemon
        return self.weakness

    def determineIfWeaknessIsSameAsStrength(self,enemyPokemonStrength):
    #Checks if the pokemons weakness is the enemy pokemons strength, leading to a true  or false
        if self.weakness == enemyPokemonStrength:
            #print("POKEMONS WEAKNESS IS THE STRENGTH OF ATTACKER")
            self.enemyPokemonStrengthIsThisPokemonsWeakness = True
        else:
            self.enemyPokemonStrengthIsThisPokemonsWeakness = False

    def attack(self):
    #Calculates the attack damage based on what the factors are
        attackDouble = int(self.damage * 1.5)
        attackhalved = int(self.damage * 0.5)

        damageRecieved = random.randint(attackhalved,attackDouble)

        if self.enemyPokemonStrengthIsThisPokemonsWeakness == True:
            #print("ENEMY HAS THE STRENGTH OF YOUR WEAKNESS. PLUS 25% DAMAGE")
            damageRecieved = (damageRecieved + (damageRecieved*.25))
            return int(damageRecieved)
        else:
            return int(damageRecieved)

    def setHpAfterAttack(self, damage):
        #sets the HP of the pokemon after an attack
        self.hp = self.hp - damage
        #print(self.hp)

    def isAlive(self):
        #Checks if the pokemon is alive
        if self.hp <= 0:
            return False
        else:
            return True

    def __str__(self):
        #this is a string formatter, not used in the game but still good to have
        return "Name:" + str(self.name) + " Type:" +  str(self.type) + " Damage:" + str(self.damage) + " HP:" + str(self.hp) + " Weakness:" + str(self.weakness)