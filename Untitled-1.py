alphabet = ['a', 'b', 'c', 'd', 'e', 'f' 'g', 'h', 'i','j', 'k','l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def encrypt(orignal_text, shift_number):
        Cypher_text = ''
        for letter in orignal_text:
          shift_position =  alphabet.index(letter) + shift_number
          shift_position %= len(alphabet)
          Cypher_text += alphabet[shift_position]
        print(f'Here is the encoded text:{Cypher_text}')

    encrypt(orignal_text=text, shift_number=shift)

elif direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def decrypt(encrypt_text, shift_number):
        cypher_text = ''
        for letter in encrypt_text:
         decrypt_number = alphabet.index(letter) - shift_number
         decrypt_number %= len(alphabet)
         cypher_text += alphabet[decrypt_number]

        print(f'Here is the encoded text: {cypher_text}')
    decrypt(encrypt_text =text, shift_number = shift)
else:
    print("invalid")