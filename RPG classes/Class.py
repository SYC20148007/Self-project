from Classes import classes
class warrior(classes):
    def __init__(self, health, mana, damage, speed, crit):
        super().__init__(health,mana,damage,speed,crit)
        self.toughness_modifier = 0.9
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

class paladin(classes):
    def __init__(self, health, mana, damage, speed, crit):
        super().__init__(health,mana,damage,speed,crit)
        self.toughness_modifier = 0.7
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

class rogue(classes):
    def __init__(self, health, mana, damage, speed, crit):
        super().__init__(health,mana,damage,speed,crit)
        self.toughness_modifier = 1
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

class mage(classes):
    def __init__(self, health, mana, damage, speed, crit):
        super().__init__(health,mana,damage,speed,crit)
        self.toughness_modifier = 1.2
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)

Rogue = classes(80,50,40,40,15)
Paladin = paladin(120,80,30,10,10)
Warrior = warrior(100,40,50,20,10)
Mage = classes(60,80,60,10,5)
