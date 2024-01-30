#day 12
#Scope

enemies = 1
player_health = 10


def increse_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1
  


enemies = increse_enemies()
print(f"enemies outside function: {enemies}")


#Local Scope
def game():

  def drink_potion():
    potion = 2
    print(f"player health inside function: {player_health}")
    print(f"potion inside function: {potion}")

  drink_potion()


game()

game_level = 3
enemies_list = ["Zombie", "Skeleton", "Slime"]


def create_enemy():
  new_enemy = None
  if game_level < 5:
    new_enemy = enemies_list[0]
    print(f"Game Level: {game_level}")
    print(f"Enemies: {new_enemy}")
  print(f"Enemies: {new_enemy}")


create_enemy()

#Global Constants
PI = 3.1415

  