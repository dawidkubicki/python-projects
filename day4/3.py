alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while (direction=='encode' or direction=='decode'):



    text = input("Type your message:\n")
    shift = int(input("Type your shift number:\n"))

    if direction=='encode':

        def encode(text, shift=0):

            encoded = ""

            for char in text:
                position = alphabet.index(char)
                encoded += alphabet[position+shift]

            return encoded
        

        print(encode(text, shift))
        

    elif direction=='decode':

        def decode(text, shift=0):

            decoded = ""

            for char in text:
                position = alphabet.index(char)
                decoded += alphabet[position-shift]

            return decoded
    
        print(decode(text, shift))


    direction = input("encode or decode | you can also put anything else to leave programm\n")

