import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
players_choice = int(
    input(
        "Whats do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "
    ))
if (players_choice >= 3 or players_choice < 0):
  print("Invalid choice, you lose!")
  quit()

print(choices[players_choice])

computers_choice = random.randint(0, 2)
print("Computer choose:")
print(choices[computers_choice])

if (players_choice == computers_choice):
  print(f"It's a tie!")
elif (players_choice == 0 and computers_choice == 1):
  print(f"You lose!")
elif (players_choice == 0 and computers_choice == 2):
  print(f"You win!")
elif (players_choice == 1 and computers_choice == 0):
  print(f"You win!")
elif (players_choice == 1 and computers_choice == 2):
  print(f"You lose!")
elif (players_choice == 2 and computers_choice == 0):
  print(f"You lose!")
elif (players_choice == 2 and computers_choice == 1):
  print(f"You win!")
