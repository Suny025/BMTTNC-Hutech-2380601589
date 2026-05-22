class VigenereCipher:
    def __init__(self):
        pass
    def vigenere_encrypt(self,plain_tect,key):
        encrypted_text=""
        key_index = 0
        for char in plain_tect:
            if char in plain_tect:
                key_shift = ord(key[key_index % len(key)].upper())-ord
                ('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A')+ key_shift)%26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a')+ key_shift)%26 + ord('a'))
                key_index+=1
            else:
                encrypted_text+=char
    def vigenere_decrypt (self, encryted_text,key):
        decrypted_text =""
        key_index =0
        for char in encryted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper())-ord
                ('A')
                if char.isupper():
                    decrypted_text += chr((ord(char)-ord('A')-key_shift)%26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char)-ord('a')-key_shift)%26 + ord('a'))           
                key_index +=1
            else:
                decrypted_text += char
        return decrypted_text