from higher_lower_files.art import logo, vs
from higher_lower_files.game_data import data
import random

random_person_a = random.choice(data)


def compare(follower_a, follower_b, guess):
  response = "A" if follower_a > follower_b else "B"
  if (response == guess or follower_a == follower_b):
    return True
  return False


def game(person_a, score=0):
  print(logo)
  print(
      f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}'
  )
  print(vs)
  person_b = random.choice(data)
  print(
      f'Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}'
  )

  choice = input("Who has more followers? Type 'A' or 'B': ").title()

  if choice != 'A' and choice != 'B':
    print("You didn't choose A or B")
    return

  if (compare(person_a["follower_count"], person_b["follower_count"], choice)):
    score += 1
    if choice == 'B':
      person_a = person_b
    print(f"You're right! Current score: {score}")
    game(person_a, score)
  else:
    print(f"Sorry, that's wrong. Final score: {score}")


game(random_person_a)
