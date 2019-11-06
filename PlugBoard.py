from Translator import Translator


class PlugBoard(Translator):
    def __init__(self,pairs):
        self.pairs = pairs.split(" ")
        self.dic = {}
        for value in self.pairs:
            self.dic[value[0]] = value[1]
            self.dic[value[1]] = value[0]

    def translate(self,value):
        if value in self.dic:
            return self.dic[value]
        return value

