class Character:
    def __init__(self, name, health=0, power=0):
        self.name = name
        self.heath = health
        self.power = power
    
    def attack(self, enemy):
        self.health -= enemy.power
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))

    def alive(self):
        self.health > 0

class Hero(Character):
    def __init__(self, health=10, power=5):
        super().__init__()

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")
        

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))


class Goblin(Character):
    def __init__(self, health=6, power=2):
        super().__init__()
    
    def print_status(self):
        print("The Goblin has %d health and %d power." % (self.health, self.power))

while self.alive():
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
        # Hero attacks goblin
        goblin_health -= hero_power
        print("You do %d damage to the goblin." % hero_power)
        if goblin_health <= 0:
            print("The goblin is dead.")
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)

    if goblin_health > 0:
        # Goblin attacks hero
        hero_health -= goblin_power
        print("The goblin does %d damage to you." % goblin_power)
        if hero_health <= 0:
            print("You are dead.")




