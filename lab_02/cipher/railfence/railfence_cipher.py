class RailFenceCipher:
    def __init__(self):
        pass

    # ================= VALIDATION =================
    def _validate(self, text, num_rails):
        # check text
        if text is None or str(text).strip() == "":
            raise ValueError("Text cannot be empty")

        # convert num_rails
        try:
            num_rails = int(num_rails)
        except:
            raise ValueError("num_rails must be an integer")

        # rule rail fence
        if num_rails < 2:
            raise ValueError("num_rails must be >= 2")

        if num_rails > len(str(text)):
            raise ValueError("num_rails cannot be greater than text length")

        return str(text), num_rails

    # ================= ENCRYPT =================
    def rail_fence_encrypt(self, plain_text, num_rails):
        plain_text, num_rails = self._validate(plain_text, num_rails)

        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return ''.join(''.join(r) for r in rails)

    # ================= DECRYPT =================
    def rail_fence_decrypt(self, cipher_text, num_rails):
        cipher_text, num_rails = self._validate(cipher_text, num_rails)

        # nếu num_rails = 1 thì không hợp lệ (đã check ở validate)

        # 1. xác định pattern zigzag
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        for _ in cipher_text:
            rail_lengths[rail_index] += 1

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # 2. chia cipher vào từng rail
        rails = []
        start = 0

        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # 3. rebuild plaintext
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in cipher_text:
            if not rails[rail_index]:
                raise ValueError("Invalid cipher text for given num_rails")

            plain_text += rails[rail_index].pop(0)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return plain_text
