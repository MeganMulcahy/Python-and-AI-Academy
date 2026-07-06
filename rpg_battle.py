import random
import time

class Character():
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.max_health = health # Store the original health
        self.strength = strength
        self.defense = defense

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        return damage_taken
    
    def heal(self):
        healed = self.health * random.randint(1, 10) / 10
        self.health += int(healed)

        if self.health > self.max_health:
            self.health = self.max_health
            
        print(f"{self.name} heals for {int(healed)} HP")
        return self.health

    def attack(self, target):
        damage = self.strength * random.randint(1, 5)
        return target.take_damage(damage)
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
class Rogue(Character):
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, target):
        dexterity = 20
        critical_hit = random.randint(1, 100) <= dexterity

        damage = self.strength * 2
        if critical_hit:
            damage *= 2
            print("*** Critical Hit ***")

        return target.take_damage(damage)

def arena_battle(player, enemy):
    print(f"\n=== {player.name} vs. {enemy.name} ===")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: {player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP")

        user_input = input("\nAttack, Heal, or Run?:  ").lower().strip()
        if user_input == "attack":
            dmg = player.attack(enemy)
            print(f"{player.name} hits {enemy.name} for {dmg}")

            if not enemy.is_alive():
                break

            dmg = enemy.attack(player)
            print(f"{enemy.name} hits {player.name} for {dmg}")
        
        elif(user_input == "heal"):
            player.heal()
            print(f"{player.name} heals for {player.health} HP")

            dmg = enemy.attack(player)
            print(f"{enemy.name} hits {player.name} for {dmg}")
        elif(user_input == "run"):
            print(f"{player.name} runs away!")
            return False
        else:
            print("Invalid input. Please choose Attack, Heal, or Run.")
        time.sleep(1)

    # Declaring the winner
    if player.is_alive():
        print(f"\n{player.name} wins!")
        return True
    else:
        print(f"\n{enemy.name} wins!")
        return False


if __name__ == "__main__":
    player = Character("Cheetah", 100, 10, 2)
    enemy = Rogue("Eevee", 100, 8, 4)
    arena_battle(player, enemy)