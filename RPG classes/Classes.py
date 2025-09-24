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
