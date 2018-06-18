class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')
   
    def encode(self, text):
        text = text.decode('utf-8')
        result = "".join(self.encode_char(i, text[i]) for i in range(len(text)))
        return result.encode('utf-8')
   
    def encode_char(self, i, c):
        """Returns the encoded value of c given it appears at position i in the text"""
        if c not in self.alphabet:
            return c
       
        print('Encoding character:', c)
        shift = self.shift_for_index(i)
        return self.shift_character(c, shift)
   
    def decode(self, text):
        text = text.decode('utf-8')
        result = "".join(self.decode_char(i, text[i]) for i in range(len(text)))
        return result.encode('utf-8')
   
    def decode_char(self, i, c):
        """Returns the decoded value of c given it appears at position i in the text"""
        if c not in self.alphabet:
            return c
       
        shift = 0 - self.shift_for_index(i)
        return self.shift_character(c, shift)
   
    def shift_for_index(self, index):
        key_character = self.key[index % len(self.key)]
        return self.alphabet.index(key_character)
   
    def shift_character(self, char, amount):
        old_index = self.alphabet.index(char)
        new_index = (old_index + amount) % len(self.alphabet)
        return self.alphabet[new_index]
    
abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)