import sys
import re
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    # ================= VALIDATION =================
    def validate(self, text, key):
        text = text.strip()
        key = key.strip()

        # check rỗng
        if not text:
            return False, "Text cannot be empty"

        if not key:
            return False, "Key cannot be empty"

        # check key là số
        if not key.isdigit():
            return False, "Key must be a number"

        key_int = int(key)

        # giống HTML: min=1 max=25
        if key_int < 1 or key_int > 25:
            return False, "Key must be between 1 and 25"

        # giống pattern="[A-Za-z ]+"
        if not re.fullmatch(r"[A-Za-z ]+", text):
            return False, "Text must contain only letters and spaces"

        # không cho toàn khoảng trắng
        if text.replace(" ", "") == "":
            return False, "Text cannot be only spaces"

        return True, ""

    # ================= ENCRYPT =================
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"

        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()

        valid, msg = self.validate(plain_text, key)
        if not valid:
            QMessageBox.warning(self, "Validation Error", msg)
            return

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setPlainText(
                    data.get("encrypted_text", "")
                )

                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Encrypt failed!")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= DECRYPT =================
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"

        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()

        valid, msg = self.validate(cipher_text, key)
        if not valid:
            QMessageBox.warning(self, "Validation Error", msg)
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setPlainText(
                    data.get("decrypted_text", "")
                )

                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.warning(self, "Error", "Decrypt failed!")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())