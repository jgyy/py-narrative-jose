"""
Hacking Incident - Debriefing
"""
from string import ascii_lowercase


def encrypt(text, shift):
    """
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    """
    encrypted_text = list(range(len(text)))
    alphabet = ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter
    return "".join(encrypted_text)


def decrypt(text, shift):
    """
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    """
    decrypted_text = list(range(len(text)))
    alphabet = ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    for i, letter in enumerate(text.lower()):
        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter
    return "".join(decrypted_text)


def brute_force(message):
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message.
            One of the printed outputs should be readable.
    """
    for num in range(26):
        print(f"Using shift value of {num}")
        print(decrypt(message, num))
        print("\n")


def main():
    """
    main function
    """
    alphabet = ascii_lowercase
    print(alphabet)
    print(list(alphabet))
    encrypt_str = encrypt("Get this message to the main server", 13)
    print(encrypt_str)
    print(decrypt(encrypt_str, 13))
    brute_force(encrypt_str)


if __name__ == "__main__":
    main()
