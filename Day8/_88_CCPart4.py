# Caesar Cipher Encryption 4
# fixing bugs
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# repeat the program
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        end_text = ""      
        for char in text:
            if char in alphabet:
                letter_location = alphabet.index(char)
                if direction == "encode":
                    end_text += alphabet[letter_location + shift]
                else:
                    end_text += alphabet[letter_location - shift]
            else:
                end_text += char
        if direction == "encode":
            print(f"Here is the encoded message: {end_text}")
        else:
            print(f"Here is the decoded message: {end_text}")

    caesar(text= text, shift=shift, direction = direction)
    restart = input("Do you want to  start new encryption? Yes or No\n").lower()
    if restart == 'no':
        should_end = True
        print("Have a nice day!")
