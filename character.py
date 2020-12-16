class Character:
    def __init__(self, name, health=0, power=0):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))
    
    def alive(self):
        return self.health > 0

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


hero = Character("Mando", 160, 5)
goblin = Character("Imperial Scum", 100 , 8)

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print("")
    print("What do you want to do?")
    print("1. fight {}".format(goblin.name))
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
        hero.attack(goblin)
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)

    if goblin.alive():
        goblin.attack(hero) 