import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    # ================= VALIDATE KEY =================
    def validate_key(self, key):
        key = key.strip()

        if not key:
            return False, "Key không được để trống!"

        if not key.isdigit():
            return False, "Key phải là số!"

        key_int = int(key)

        if key_int <= 1:
            return False, "Key phải lớn hơn 1!"

        return True, ""

    # ================= ENCRYPT =================
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"

        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        # validate key
        valid, msg = self.validate_key(key)
        if not valid:
            QMessageBox.warning(self, "Error", msg)
            return

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("\n=== ENCRYPT CLICKED ===")
            print(f"Payload: {payload}")
            print("Status:", response.status_code)
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
                    response.text
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    # ================= DECRYPT =================
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"

        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        # validate key
        valid, msg = self.validate_key(key)
        if not valid:
            QMessageBox.warning(self, "Error", msg)
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            print("\n=== DECRYPT CLICKED ===")
            print(f"Payload: {payload}")
            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setPlainText(
                    data.get("decrypted_text", "")
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
                    response.text
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