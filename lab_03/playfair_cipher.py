import sys
import requests

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from ui.playfair import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(
            self.call_api_encrypt
        )

        self.ui.btn_decrypt.clicked.connect(
            self.call_api_decrypt
        )

    def call_api_encrypt(self):

        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        # Validate Plain Text
        if plain_text == "":
            QMessageBox.warning(
                self,
                "Error",
                "Plain Text không được để trống!"
            )
            return

        # Validate Key
        if key == "":
            QMessageBox.warning(
                self,
                "Error",
                "Key không được để trống!"
            )
            return

        if not key.isalpha():
            QMessageBox.warning(
                self,
                "Error",
                "Key chỉ được chứa chữ cái A-Z!"
            )
            return

        url = "http://127.0.0.1:5000/api/playfair/encrypt"

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(
                url,
                json=payload
            )

            # ================== POWER SHELL LOG ==================
            print("\n=== ENCRYPT CLICKED ===")
            print(f"Payload: {{'plain_text': '{plain_text}', 'key': '{key}'}}")
            print(f"Status: {response.status_code}")
            print("Response:")
            print(response.text)
            # =====================================================

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
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def call_api_decrypt(self):

        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        # Validate Cipher Text
        if cipher_text == "":
            QMessageBox.warning(
                self,
                "Error",
                "Cipher Text không được để trống!"
            )
            return

        # Validate Key
        if key == "":
            QMessageBox.warning(
                self,
                "Error",
                "Key không được để trống!"
            )
            return

        if not key.isalpha():
            QMessageBox.warning(
                self,
                "Error",
                "Key chỉ được chứa chữ cái A-Z!"
            )
            return

        url = "http://127.0.0.1:5000/api/playfair/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(
                url,
                json=payload
            )

            # ================== POWER SHELL LOG ==================
            print("\n=== DECRYPT CLICKED ===")
            print(f"Payload: {{'cipher_text': '{cipher_text}', 'key': '{key}'}}")
            print(f"Status: {response.status_code}")
            print("Response:")
            print(response.text)
            # =====================================================

            if response.status_code == 200:

                data = response.json()

                decrypted_text = data.get(
                    "decrypted_text",
                    ""
                )

                # API báo lỗi
                if decrypted_text == "INVALID_CIPHER_TEXT":
                    QMessageBox.warning(
                        self,
                        "Error",
                        "Cipher Text không hợp lệ!"
                    )
                    return

                self.ui.txt_plain_text.setPlainText(
                    decrypted_text
                )

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
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())