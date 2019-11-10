from Translator import Translator

class Rotor(Translator):


    def __init__(self,forward_permutation, ring_setting, turnover):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.forward_permutation = [value for value in forward_permutation]
        self.ring_setting = self.toIndex(ring_setting)
        self.turnover = self.toIndex(turnover)
    def toIndex(self,letter):
        return (self.alphabet.find(letter)+1)
    def toLetter(self,index):
        return self.alphabet[index-1]

    def set_position(self):
        next_position = (self.ring_setting+1) % 26
        self.ring_setting = next_position

    def turnoverCheck(self):
        return self.ring_setting == self.turnover

    def translate(self,value):
        return self.forward_permutation[self.toIndex(value)]

    def revTranslate(self,value):
        return self.alphabet[self.forward_permutation.index(value)]
