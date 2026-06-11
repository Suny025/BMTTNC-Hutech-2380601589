class VigenereCipher:
    def __init__(self):
        pass

    # ================= VALIDATION =================
    def _validate(self, text, key):
        if text is None or str(text).strip() == "":
            raise ValueError("Text cannot be empty")

        if key is None or str(key).strip() == "":
            raise ValueError("Key cannot be empty")

        # lọc chỉ chữ cái
        clean_key = "".join([c for c in key if c.isalpha()])

        if len(clean_key) == 0:
            raise ValueError("Key must contain letters A-Z")

        return str(text), clean_key.upper()

    # ================= ENCRYPT =================
    def vigenere_encrypt(self, plain_text, key):
        plain_text, key = self._validate(plain_text, key)

        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():

                key_shift = ord(key[key_index % len(key)]) - ord('A')

                if char.isupper():
                    encrypted_text += chr(
                        (ord(char) - ord('A') + key_shift) % 26 + ord('A')
                    )
                else:
                    encrypted_text += chr(
                        (ord(char) - ord('a') + key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                encrypted_text += char

        return encrypted_text

    # ================= DECRYPT =================
    def vigenere_decrypt(self, encrypted_text, key):
        encrypted_text, key = self._validate(encrypted_text, key)

        decrypted_text = ""
        key_index = 0

        for char in encrypted_text:
            if char.isalpha():

                key_shift = ord(key[key_index % len(key)]) - ord('A')

                if char.isupper():
                    decrypted_text += chr(
                        (ord(char) - ord('A') - key_shift) % 26 + ord('A')
                    )
                else:
                    decrypted_text += chr(
                        (ord(char) - ord('a') - key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text