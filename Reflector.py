from Translator import Translator

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Reflector(Translator):
    def __init__(self):
        self.B = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    def translate(self,val):
        for i in range(len(alphabet)):
            if val == alphabet[i]:
                return self.B[i]