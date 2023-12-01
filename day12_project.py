from guess_a_number.art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def dificulty_level():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  turns = EASY_LEVEL_TURNS if difficulty == "easy" else HARD_LEVEL_TURNS
  return turns


def check_guess(guess, number):
  if guess == number:
    print("You got it right!")
    return True
  elif guess < number:
    print("Too low.")
  else:
    print("Too high.")
  return False


attempts = dificulty_level()
while attempts > 0:
  print(f"You have {attempts} attempts left.")
  guess = int(input("Make a guess: "))
  if check_guess(guess, number):
    break
  attempts -= 1
  if attempts == 0:
    print("You ran out of attempts. You lose.")
    print(f"The answer was {number}")
