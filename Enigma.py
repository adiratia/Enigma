from PlugBoard import PlugBoard
from Reflector import Reflector
from Substitutor import Substitutor
from Rotor import Rotor

class Enigma(Substitutor):

    def __init__(self, plug_board_pairs, rotors):
        self.plugboard = PlugBoard(plug_board_pairs)
        self.rotors = [Rotor(rotor[0], rotor[1], rotor[2]) for rotor in rotors]
        self.reflector = Reflector()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encrypt_char(self,letter):
        encryptedLetter = self.plugboard.translate(letter)
        self.rotors[0].set_position()
        if self.rotors[0].turnoverCheck():
            self.rotors[1].set_position()
            if self.rotors[1].turnoverCheck():
                    self.rotors[2].set_position()
        '''
        #forward
        encryptedLetter = self.rotors[0].encrypt_forward(encryptedLetter, self.wordCount)
        difference = (self.rotors[0].ring_setting - self.rotors[1].ring_setting) % 26
        encryptedLetter = self.rotors[1].encrypt_forward(self.alphabet[self.alphabet.index(encryptedLetter)], 0 - difference)
        difference = (self.rotors[1].ring_setting - self.rotors[2].ring_setting) % 26
        encryptedLetter = self.rotors[2].encrypt_forward(self.alphabet[self.alphabet.index(encryptedLetter)], 0 - difference)
        encryptedLetter = self.reflector.translate(encryptedLetter)
        print("After Reflector: " , encryptedLetter)
        #backward
        encryptedLetter = self.rotors[2].encrypt_backward(encryptedLetter, 0)
        difference = (self.rotors[1].ring_setting - self.rotors[2].ring_setting) % 26
        encryptedLetter = self.rotors[1].encrypt_backward(self.alphabet[self.alphabet.index(encryptedLetter) - difference], 0)
        difference = (self.rotors[0].ring_setting - self.rotors[1].ring_setting) % 26
        encryptedLetter = self.rotors[0].encrypt_backward(self.alphabet[self.alphabet.index(encryptedLetter) - self.wordCount], 0)
        encryptedLetter = self.plugboard.translate(encryptedLetter)

        self.wordCount = (self.wordCount + 1) % 26

        '''

        ### FORWARD ###
        difference = self.rotors[0].ring_setting
        encryptedLetter = self.rotors[0].encrypt_forward(encryptedLetter, difference)
        difference = (self.rotors[1].ring_setting - self.rotors[0].ring_setting) % 26
        encryptedLetter = self.rotors[1].encrypt_forward(encryptedLetter, difference)
        difference = (self.rotors[2].ring_setting - self.rotors[1].ring_setting) % 26
        encryptedLetter = self.rotors[2].encrypt_forward(encryptedLetter, difference)
        encryptedLetter = self.reflector.translate(encryptedLetter)

        ### BACKWARD ###
        difference = self.rotors[2].ring_setting
        encryptedLetter = self.rotors[2].encrypt_backward(encryptedLetter, difference)
        difference = (self.rotors[1].ring_setting - self.rotors[2].ring_setting) % 26
        encryptedLetter = self.rotors[1].encrypt_backward(encryptedLetter, difference)
        difference = (self.rotors[0].ring_setting - self.rotors[1].ring_setting) % 26
        encryptedLetter = self.rotors[0].encrypt_backward(encryptedLetter, difference)
        encryptedLetter = self.alphabet[(self.alphabet.index(encryptedLetter) - self.rotors[0].ring_setting) % 26]
        encryptedLetter = self.plugboard.translate(encryptedLetter)

        return encryptedLetter

