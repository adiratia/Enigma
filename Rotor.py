from Translator import Translator

class Rotor(Translator):

    def __init__(self, forward_permutation, ring_setting, turnover):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.forward_permutation = [value for value in forward_permutation]
        self.ring_setting = self.toIndex(ring_setting)
        self.turnover = self.toIndex(turnover)

    def toIndex(self,letter):
        return self.alphabet.find(letter)

    def toLetter(self,index):
        return self.alphabet[index]

    def set_position(self):
        self.ring_setting = (self.ring_setting + 1) % 26

    def turnoverCheck(self):
        return self.ring_setting == (self.turnover + 1)

    def encrypt_forward(self, value, difference):
        return self.forward_permutation[(self.toIndex(value) + difference) % 26]

    def encrypt_backward(self, value, difference):
        return self.alphabet[self.forward_permutation.index(self.alphabet[(self.alphabet.index(value) + difference) % 26])]
