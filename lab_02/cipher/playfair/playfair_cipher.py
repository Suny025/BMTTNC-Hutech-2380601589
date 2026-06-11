class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")

        # bỏ ký tự trùng trong key
        new_key = ""
        for c in key:
            if c.isalpha() and c not in new_key:
                new_key += c

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for c in alphabet:
            if c not in new_key:
                new_key += c

        matrix = [list(new_key[i:i + 5]) for i in range(0, 25, 5)]

        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def prepare_plain_text(self, text):
        text = text.upper().replace("J", "I")
        text = ''.join(c for c in text if c.isalpha())

        result = ""
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 < len(text):
                b = text[i + 1]

                # 2 ký tự giống nhau => chèn X
                if a == b:
                    result += a + "X"
                    i += 1
                else:
                    result += a + b
                    i += 2
            else:
                result += a + "X"
                i += 1

        if len(result) % 2 != 0:
            result += "X"

        return result

    def playfair_encrypt(self, plain_text, matrix):

        plain_text = self.prepare_plain_text(plain_text)

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):

            a = plain_text[i]
            b = plain_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:

                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]

            elif col1 == col2:

                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]

            else:

                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):

        cipher_text = cipher_text.upper()
        cipher_text = ''.join(c for c in cipher_text if c.isalpha())

        if len(cipher_text) % 2 != 0:
            return "INVALID_CIPHER_TEXT"

        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):

            a = cipher_text[i]
            b = cipher_text[i + 1]

            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:

                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]

            elif col1 == col2:

                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]

            else:

                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # bỏ X được chèn giữa 2 ký tự giống nhau
        result = ""

        i = 0
        while i < len(decrypted_text):

            if (
                i + 2 < len(decrypted_text)
                and decrypted_text[i] == decrypted_text[i + 2]
                and decrypted_text[i + 1] == "X"
            ):
                result += decrypted_text[i]
                i += 2
            else:
                result += decrypted_text[i]
                i += 1

        if result.endswith("X"):
            result = result[:-1]

        return result