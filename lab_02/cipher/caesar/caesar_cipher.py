from cipher.caesar import ALPHABET


class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
        self.alphabet_len = len(self.alphabet)

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        encrypted_text = []

        for letter in text:
            # ❌ nếu không nằm trong bảng chữ cái -> giữ nguyên
            if letter not in self.alphabet:
                encrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % self.alphabet_len
            encrypted_text.append(self.alphabet[output_index])

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        decrypted_text = []

        for letter in text:
            # ❌ nếu không nằm trong bảng chữ cái -> giữ nguyên
            if letter not in self.alphabet:
                decrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % self.alphabet_len
            decrypted_text.append(self.alphabet[output_index])

        return "".join(decrypted_text)