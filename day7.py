#day7
#hangman project

import random
from hangman_files.hangman_words import word_list
from hangman_files.hangman_art import stages, logo


end_of_game = False 

lives = 6

chosen_world = random.choice(word_list)
print(logo)
world_length = len(chosen_world)

display = []

for blanks in range(world_length):
  display += "_"



while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print("You have already guessed that letter.")
  
  for position in range(world_length):
    letter = chosen_world[position]
    if(letter == guess):
      display[position] = guess

  if(guess not in chosen_world):
    print("The letter is not in the word")
    lives -= 1
    
  print(f"{stages[lives]}")
  print(f"{' '.join(display)}")
  
  if("_" not in display):
    end_of_game = True
    print("you win!")
  elif(lives == 0):
    end_of_game = True
    print("you lose!")
    print(f"The word was {chosen_world}")