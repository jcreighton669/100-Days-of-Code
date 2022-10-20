from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_count, cipher_direction):
    output_string = ""
    if cipher_direction == "decode":
        shift_count *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_count
            output_string += alphabet[new_position]
        else:
            output_string += letter
    print(f"The {cipher_direction}d text is {output_string}")

print(logo)

should_contiue = True
while should_contiue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)

    result = input("Type 'yes' if you ant to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_contiue = False
        print("Goodbye")