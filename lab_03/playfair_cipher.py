import sys
import re
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    # ================= VALIDATION =================
    def validate(self, text, key):
        text = text.strip().upper()
        key = key.strip().upper()

        if not text:
            return False, "Text không được để trống!"

        if not key:
            return False, "Key không được để trống!"

        if not key.isalpha():
            return False, "Key chỉ được chứa chữ cái A-Z!"

        # chỉ chữ + space
        if not re.fullmatch(r"[A-Z ]+", text):
            return False, "Text chỉ được chứa chữ cái và khoảng trắng!"

        return True, ""

    # ================= ENCRYPT =================
    def call_api_encrypt(self):

        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()

        # validate
        valid, msg = self.validate(plain_text, key)
        if not valid:
            QMessageBox.warning(self, "Error", msg)
            return

        # normalize (QUAN TRỌNG PLAYFAIR)
        plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
        key = key.upper().replace("J", "I")

        url = "http://127.0.0.1:5000/api/playfair/encrypt"

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("\n=== ENCRYPT CLICKED ===")
            print(f"Payload: {payload}")
            print(f"Status: {response.status_code}")
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setPlainText(
                    data.get("encrypted_text", "")
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Encrypted Successfully"
                )
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"API Error: {response.status_code}"
                )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= DECRYPT =================
    def call_api_decrypt(self):

        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()

        # validate
        valid, msg = self.validate(cipher_text, key)
        if not valid:
            QMessageBox.warning(self, "Error", msg)
            return

        # normalize
        cipher_text = cipher_text.upper().replace("J", "I").replace(" ", "")
        key = key.upper().replace("J", "I")

        url = "http://127.0.0.1:5000/api/playfair/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("\n=== DECRYPT CLICKED ===")
            print(f"Payload: {payload}")
            print(f"Status: {response.status_code}")
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()

                decrypted_text = data.get("decrypted_text", "")

                if decrypted_text == "INVALID_CIPHER_TEXT":
                    QMessageBox.warning(
                        self,
                        "Error",
                        "Cipher Text không hợp lệ!"
                    )
                    return

                self.ui.txt_plain_text.setPlainText(decrypted_text)

                QMessageBox.information(
                    self,
                    "Success",
                    "Decrypted Successfully"
                )
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    f"API Error: {response.status_code}"
                )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())