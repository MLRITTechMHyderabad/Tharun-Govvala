class Character:
    def __init__(self,name,health,power,defence,speed):
        self.name=name 
        self.health=health
        self.attack_power=power
        self.defense=defence
        self.speed=speed
    def attack(self,target):
        target.take_damage(self.attack_power)

    def take_damage(self,amount):
        self.health=self.health-amount

    def is_alive(self):
        if(self.health<=0):
            return False
        return True
        
class Warrior(Character):
    def __init__(self,rage,name,health,power,defence,speed):
        super().__init__(name,health,power,defence,speed)
        self.rage=rage
    
    def Berserk_Mode(self):
        if(self.health<30):
            self.health=self.health-(2*self.attack_power)

class Mage(Character):
    
    def __init__(self,mana,name,health,power,defence,speed):
        super().__init__(name,health,power,defence,speed)
        self.mana=mana
    def Fire_Ball(self):
        self.health=self.health+self.mana

        

class Archer(Character):
    def __init__(self,critical_chance,name,health,power,defence,speed):
        super().__init__(name,health,power,defence,speed)
        self.critical_chance=critical_chance
    
    def Precision_Shot(self):
        if(self.critical_chance<=30):
            self.attack_power=self.attack_power*2

warrior = Warrior("Alex",100,15,100,13)
mage = Mage("Mage",100,18,100,43)
archer = Archer("ranged attack",100,21,100,11)

while(warrior.health>0 or mage.healtk>0 or archer.health>0):
    if(warrior.health>0):
        if(mage.health<=0 and archer.health):
            print()






    

