
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher


app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = int(data['key'])

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)

    return jsonify({
        'encrypted_text': encrypted_text
    })


@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = int(data['key'])

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)

    return jsonify({
        'decrypted_text': decrypted_text
    })



# Vigenere
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = data['key']

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)

    return jsonify({
        'encrypted_text': encrypted_text
    })


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = data['key']

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)

    return jsonify({
        'decrypted_text': decrypted_text
    })
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():

    data = request.get_json()

    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({
            'error': 'Missing plain_text or key'
        }), 400

    encrypted_text = railfence_cipher.rail_fence_encrypt(
        plain_text,
        int(key)
    )

    return jsonify({
        'encrypted_text': encrypted_text
    })

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():

    data = request.get_json()

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({
            'error': 'Missing cipher_text or key'
        }), 400

    decrypted_text = railfence_cipher.rail_fence_decrypt(
        cipher_text,
        int(key)
    )

    return jsonify({
        'decrypted_text': decrypted_text
    })


playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()

    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    return jsonify({
        'playfair_matrix': playfair_matrix
    })


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()

    plain_text = data['plain_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    encrypted_text = playfair_cipher.playfair_encrypt(
        plain_text,
        playfair_matrix
    )

    return jsonify({
        'encrypted_text': encrypted_text
    })


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()

    cipher_text = data['cipher_text']
    key = data['key']

    playfair_matrix = playfair_cipher.create_playfair_matrix(key)

    decrypted_text = playfair_cipher.playfair_decrypt(
        cipher_text,
        playfair_matrix
    )

    return jsonify({
        'decrypted_text': decrypted_text
    })




if __name__ == '__main__':
    app.run(debug=True, port=5000)

