# A text-based Python program to convert Strings into Morse Code.
MORSE_DICT = {
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "0": "-----",
  "?": "..--..",
  "!": "-.-.--",
  ".": "-.-.--",
  ",": "--..--",
  ";": "-.-.-.",
  ":": "---...",
  "+": ".-.-.",
  "-": "-....-",
  "/": "-..-.",
  "=": "-...-",
}

def textToMorse():
    string=input('Enter a String: ').upper()
    morse = [MORSE_DICT[letter] for letter in string]
    return "".join(morse)

def morseToText():
    morse=input('Enter a Morse: ').split(' ')
    morse_to_char = { morse:char for (char,morse) in MORSE_DICT.items() }
    string = [morse_to_char[code] for code in morse]
    return "".join(string)



again = "yes"

print("Welcome!")
while again != "no":
    choice = input("Tap 1 to Morse to Text or 2 to Text to Morse: ")
    if choice=='1':
        morse = textToMorse()
        print("Morse Code: ", morse)
    elif choice=='2':
        text = morseToText()
        print("Text: ", text)
    else:
        print("Invalid choice")

    again = input("Continue? Tap 'yes' or 'no'. ")

print("Thanks for using!")
    
    # [ state for state in all_states if state not in guessed_states]