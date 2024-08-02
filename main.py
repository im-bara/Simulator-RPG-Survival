import random

#Player_Stats
player = {
    'name': '',
    'health': 100,
    'strength': 10,
    'defense': 5,
    'inventory': []
}

#Enemy_Stats
enemies = [
    {'name': 'Goblin', 'health': 30, 'strength': 5},
    {'name': 'Orc', 'health': 50, 'strength': 10},
    {'name': 'Dragon', 'health': 100, 'strength': 20}
]

def print_status():
    print(f"{player['name']}'s Health: {player['health']}")
    print("Inventory:", player['inventory'])

def attack(enemy):
    damage = player['strength'] - enemy['health'] // 10
    enemy['health'] -= max(damage, 0)
    print(f"You attacked the {enemy['name']} and dealt {damage} damage!")

def enemy_attack(enemy):
    damage = enemy['strength'] - player['defense'] // 2
    player['health'] -= max(damage, 0)
    print(f"The {enemy['name']} attacked you and dealt {damage} damage!")

def find_item():
    items = ['Health Potion', 'Sword', 'Shield']
    found_item = random.choice(items)
    player['inventory'].append(found_item)
    print(f"You found a {found_item}!")

def rest():
    player['health'] = min(100, player['health'] + 20)
    print("You rested and regained some health.")

def game_loop():
    print("Welcome to the survival RPG!")
    player['name'] = input("Enter your character's name: ")

    while player['health'] > 0:
        print_status()
        action = input("What do you want to do? (explore/rest/status/quit): ").lower()

        if action == 'explore':
            encounter_chance = random.randint(1, 10)
            if encounter_chance > 3:
                enemy = random.choice(enemies)
                print(f"A wild {enemy['name']} appears!")
                while enemy['health'] > 0 and player['health'] > 0:
                    fight_action = input("Do you want to attack or run? ").lower()
                    if fight_action == 'attack':
                        attack(enemy)
                        if enemy['health'] > 0:
                            enemy_attack(enemy)
                    elif fight_action == 'run':
                        print("You ran away safely.")
                        break
                    else:
                        print("Invalid action!")
                if player['health'] <= 0:
                    print("You have been defeated!")
                    break
                elif enemy['health'] <= 0:
                    print(f"You defeated the {enemy['name']}!")
            else:
                find_item()

        elif action == 'rest':
            rest()

        elif action == 'status':
            print_status()

        elif action == 'quit':
            print("Thanks for playing!")
            break

        else:
            print("Invalid action!")

    if player['health'] <= 0:
        print("Game Over!")

# Start the game
game_loop()
