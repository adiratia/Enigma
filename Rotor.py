from Translator import Translator

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Rotor(Translator):


    def __init__(self,forward_permutation, ring_setting, turnover):
        self.forward_permutation = [value for value in forward_permutation]
        self.ring_setting = ring_setting
        self.turnover = turnover
    def set_position(self):
        next_position = (( alphabet.find(self.ring_setting))+1) % 25
        self.ring_setting = alphabet[next_position]

    def turnoverCheck(self):
        if self.ring_setting == self.turnover:
            return True
        return False

    def translate(self,value):
        print((alphabet.find(self.ring_setting)))
        print((alphabet.find(value)))
        position = (alphabet.find(self.ring_setting) + alphabet.find(value)-1)% 25
        return self.forward_permutation[position]

    def revTranslate(self,value):
        position = ( self.forward_permutation.index(value) + self.forward_permutation.index(self.ring_setting)) % 25
        return alphabet[position]