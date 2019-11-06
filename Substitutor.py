from abc import ABC


class  Substitutor(ABC):
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def toIndex(self,letter):
        return (self.alphabet.find(letter)+1)
    def toLetter(self,index):
        return self.alphabet[index-1]





