from Enigma import Enigma

def driver():
    rotors=[('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'A', 'V'),
            ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'A', 'E'),
            ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')]
    enigma=Enigma('AB CD',rotors)
    print(enigma.encrypt_char('A'))





driver()