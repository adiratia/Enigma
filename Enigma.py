from PlugBoard import PlugBoard
from Reflector import Reflector
from Substitutor import Substitutor
from Rotor import Rotor


class Enigma(Substitutor):
    def __init__(self,plug_board_pairs,rotors):
        self.plugboard=PlugBoard(plug_board_pairs)
        self.rotors=[Rotor(rotor[0], rotor[1], rotor[2]) for rotor in rotors]
        self.reflector=Reflector()
    def encrypt_char(self,letter):
        encryptedLetter=self.plugboard.translate(letter)
        self.rotors[0].set_position()
        if self.rotors[0].turnoverCheck():
            self.rotors[1].set_position()
            if self.rotors[1].turnoverCheck():
                    self.rotors[2].set_position()
        encryptedLetter=self.rotors[0].translate(encryptedLetter)
        encryptedLetter=self.rotors[1].translate(encryptedLetter)
        encryptedLetter=self.rotors[2].translate(encryptedLetter)
        self.reflector.translate(encryptedLetter)
        encryptedLetter=self.rotors[2].revTranslate(encryptedLetter)
        encryptedLetter=self.rotors[1].revTranslate(encryptedLetter)
        encryptedLetter=self.rotors[0].revTranslate(encryptedLetter)
        encryptedLetter=self.plugboard.translate(encryptedLetter)
        return encryptedLetter

