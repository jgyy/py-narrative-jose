"""
Final Field Readiness Test - Solutions
"""
from string import ascii_lowercase
from random import sample, seed


class Encryption:
    """
    encryption class
    """

    def __init__(self, rseed):
        seed(rseed)
        self.seed = rseed
        self.encrypted_phrase = ""
        self.true_alphabet = list(ascii_lowercase)
        self.rand_alphabet = sample(self.true_alphabet, len(self.true_alphabet))

    def encryption(self, message):
        """
        This method will take in a string message and encrypt it. Check the video or
        the instructions above in the markdown for full description of how your
        decryption method should work.
        """
        output = ""
        for i in message:
            output += i
            output += sample(self.true_alphabet, 1)[0]
        self.encrypted_phrase = output[::-1]
        encrypted_phase_two = list(range(len(self.encrypted_phrase)))
        for i, letter in enumerate(self.encrypted_phrase.lower()):
            if letter in self.true_alphabet:
                index = self.true_alphabet.index(letter)
                encrypted_phase_two[i] = self.rand_alphabet[index]
            else:
                encrypted_phase_two[i] = letter
        self.encrypted_phrase = "".join(encrypted_phase_two)
        return self.encrypted_phrase

    def decryption(self, message, rseed):
        """
        This method takes in a messsage and a seed for the random shuffled alphabet.
        It then returns the decrypted alphabet.
        """
        seed(rseed)
        session_rand_alphabet = sample(self.true_alphabet, len(self.true_alphabet))
        decrypted_message = list(range(len(message)))
        for i, letter in enumerate(message.lower()):
            if letter in self.true_alphabet:
                index = session_rand_alphabet.index(letter)
                decrypted_message[i] = self.true_alphabet[index]
            else:
                decrypted_message[i] = letter
        decrypted_message = "".join(decrypted_message)[::-1][::2]
        return decrypted_message


def main():
    """
    main function
    """
    enc = Encryption(20)
    ency = enc.encryption("hello world")
    print(ency)
    print(enc.decryption(ency, 20))


if __name__ == "__main__":
    main()
