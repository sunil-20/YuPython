# Caesar Cipher Encryption 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift, direction):
    message_after_encrypt = ""
    for i in text:
        if direction == "encode":
            letter_location = alphabet.index(i)
            message_after_encrypt += alphabet[letter_location + shift]
        else:
            letter_location = letter_location = alphabet.index(i)
            message_after_encrypt += alphabet[letter_location - shift]
    print(message_after_encrypt)

encrypt(text= text, shift=shift, direction = direction)