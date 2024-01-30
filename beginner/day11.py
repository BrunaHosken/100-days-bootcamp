#day 11
#blackjack capstone

from blackjack_files.art import logo
from replit import clear
import random


def deal_card():
  """Returns a random card from the deck.""" ""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0, len(cards) - 1)]


def calculate(cards):
  """Takes a list of cards and returns the sum of the cards.""" ""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards[cards.index(11)] = 1
    return sum(cards)

  return sum(cards)


def compare(user_card, dealer_card):
  """Takes two card sums and returns a string that declares the winner.""" ""
  if user_card == dealer_card:
    return "You tied!"
  elif dealer_card == 0 or user_card > 21:
    return "You busted! Dealer wins!"
  elif dealer_card > 21 or user_card == 0:
    return "Dealer busted! You win!"
  elif user_card > dealer_card:
    return "You win!"
  else:
    return "You lose! Dealer wins!"


def blackjack():
  """Starts a game of blackjack. """
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  user_score = 0
  computer_score = 0

  for _ in range(0, 2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    computer_score = calculate(computer_cards)
    print(f"Computers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    print("Computer is drawing a card")
    computer_cards.append(deal_card())
    computer_score = calculate(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(
      f"Computers final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()
print(f"Okay, maybe next time.")
