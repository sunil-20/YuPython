# Caesar Cipher Encryption 1
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    end_text = ""
    for i in text:
        letter_location = alphabet.index(i)
        if direction == "encode":
            end_text += alphabet[letter_location + shift]
        else:
            end_text += alphabet[letter_location - shift]
    if direction == "encode":
        print(f"Here is the encoded message: {end_text}")
    else:
        print(f"Here is the decoded message: {end_text}")

caesar(text= text, shift=shift, direction = direction)