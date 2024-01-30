#day8 project
#Caesar Cipher

from caesar_files.art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = "yes"  

print(logo)

def caesar(text, shift, direction):
    if(direction == "encode" or direction == "decode"):
        alphabet_printed = ""
        if direction == "decode":
            shift *= -1
        if direction == "encode":
            alphabet_len = -1
        
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                shifted_index = letter_index + shift
                if shifted_index > 25:
                    shifted_index += 26 * alphabet_len
                    alphabet_printed += alphabet[shifted_index]
                else:
                    alphabet_printed += alphabet[shifted_index]
            else:
                alphabet_printed += letter
        print(f"Your {direction}d text is: {alphabet_printed}")
    else:
        print(f"Invalid option, please try again")
        
 
while again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(text, shift, direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Thanks for using the Caesar Cipher!")
