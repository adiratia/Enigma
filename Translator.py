from abc import abstractmethod

from Substitutor import Substitutor

class Translator(Substitutor):
    def __init__(self,text):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.text = text
