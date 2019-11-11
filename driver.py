from Enigma import Enigma

def driver():
    rotors=[('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'T', 'V'),
            ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'Y', 'E'),
            ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'A', 'Q')]
    enigma = Enigma('AB CD',rotors)
    #print(enigma.encrypt_char('A'))
    print("Plugboard: ", enigma.plugboard.pairs)
    plaintext = input("Enter plain text: ")
    print("Plaintext: " ,plaintext)
    print("Ciphertext: ", end='')
    for i in range(len(plaintext)):
        if 'A' <= plaintext[i] <= 'Z':
            print(enigma.encrypt_char(plaintext[i]), end='')

driver()