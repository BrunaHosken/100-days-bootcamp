from replit import clear
from secret_auction_files.art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is you name?: ")
  bid = int(input("What's your bid?: "))
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  bids[name] = bid

  if should_continue == "no":
    bidding_finished = True
  else:
    clear()

highest_bid = 0
name_highest_bid = ""

for bidder in bids:
  if bids[bidder] > highest_bid:
    highest_bid = bids[bidder]
    name_highest_bid = bidder

print(f"The winner is {name_highest_bid} with a bid of ${highest_bid}.")
