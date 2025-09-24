class classes:
    def __init__(self, health,mana, damage, speed, crit,):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.speed = speed
        self.crit = crit

    def double_health(self):
        self.health *= 2
    def double_damage(self):
        self.damage *= 2
    def double_speed(self):
        self.speed *= 2
    def double_crit(self):
        self.crit *= 2
    def take_damage(self, amount):
        self.health -= amount

class warrior(classes):
    def __init__(self, health, mana, damage, speed, crit):
        super().__init__(health,mana,damage,speed,crit)
        self.toughness_modifier = 0.9
    def take_damage(self, amount):
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)


Rouge = classes(80,50,40,40,15)
Paladin = classes(120,80,30,10,10)
Warrior = warrior(100,40,50,20,10)
Mage = classes(60,80,60,10,5)


print(Rouge.health)
Rouge.double_damage()
print("Warrior health",Warrior.health)
Warrior.take_damage(80)
print("Warrior health",Warrior.health)