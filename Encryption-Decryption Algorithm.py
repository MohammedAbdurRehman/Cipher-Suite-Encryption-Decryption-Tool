import random
import base64

# Helper functions to encode/decode with Base64 for safe output
def base64_encode(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def base64_decode(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

# 1. Vernam Cipher
def vernam_cipher_encrypt(plain_text, key):
    cipher_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(plain_text, key))
    return base64_encode(cipher_text)

def vernam_cipher_decrypt(cipher_text, key):
    decoded_cipher = base64_decode(cipher_text)
    plain_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(decoded_cipher, key))
    return plain_text

# 2. Caesar Cipher
def caesar_cipher_encrypt(plain_text, shift):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            cipher_text += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            cipher_text += char
    return cipher_text

def caesar_cipher_decrypt(cipher_text, shift):
    return caesar_cipher_encrypt(cipher_text, -shift)

# 3. Transposition Cipher
def transposition_cipher_encrypt(plain_text, key):
    cipher_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plain_text):
            cipher_text[col] += plain_text[pointer]
            pointer += key
    return ''.join(cipher_text)

def transposition_cipher_decrypt(cipher_text, key):
    num_cols = len(cipher_text) // key
    num_rows = key
    num_extra = len(cipher_text) % key
    plain_text = [''] * num_cols
    col, row = 0, 0

    for symbol in cipher_text:
        plain_text[col] += symbol
        col += 1
        if (col == num_cols or (col == num_cols - 1 and row >= num_extra)):
            col = 0
            row += 1
    return ''.join(plain_text)

# 4. Stream Cipher
def stream_cipher_encrypt(plain_text, seed):
    random.seed(seed)
    cipher_text = ''.join(chr(ord(c) ^ random.randint(0, 255)) for c in plain_text)
    return base64_encode(cipher_text)

def stream_cipher_decrypt(cipher_text, seed):
    random.seed(seed)
    decoded_cipher = base64_decode(cipher_text)
    plain_text = ''.join(chr(ord(c) ^ random.randint(0, 255)) for c in decoded_cipher)
    return plain_text

# 5. Block Cipher (Basic ECB Mode with XOR and a block size of 8)
def block_cipher_encrypt(plain_text, key):
    block_size = 8
    cipher_text = ''
    for i in range(0, len(plain_text), block_size):
        block = plain_text[i:i + block_size]
        cipher_text += vernam_cipher_encrypt(block, key[:len(block)])
    return cipher_text

def block_cipher_decrypt(cipher_text, key):
    block_size = 8
    plain_text = ''
    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i + block_size]
        plain_text += vernam_cipher_decrypt(block, key[:len(block)])
    return plain_text

# Interactive Key Selection
def select_key(cipher_name):
    if cipher_name == "Vernam":
        keys = ["XMCKL", "GHIJK", "ABCDE"]
    elif cipher_name == "Caesar":
        keys = [3, 5, 7]
    elif cipher_name == "Transposition":
        keys = [4, 6, 8]
    elif cipher_name == "Stream":
        keys = [42, 101, 2024]
    elif cipher_name == "Block":
        keys = ["MYSECRET", "ANOTHERK", "BLOCKKEY"]
    print(f"Available keys for {cipher_name} Cipher: {keys}")
    selected_key = input(f"Select one key from the above (enter exactly as shown for Vernam/Block or a number for others): ")
    if cipher_name in ["Vernam", "Block"]:
        return selected_key
    else:
        return int(selected_key)

# Interactive Encryption/Decryption Selection
def cipher_menu():
    while True:
        print("\nSelect the Encryption/Decryption Technique:")
        print("1. Vernam Cipher")
        print("2. Caesar Cipher")
        print("3. Transposition Cipher")
        print("4. Stream Cipher")
        print("5. Block Cipher")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting...")
            break
        
        text = input("\nEnter the text to encrypt/decrypt: ")

        if choice == '1':  # Vernam Cipher
            key = select_key("Vernam")
            operation = input("Encrypt or Decrypt? (e/d): ").lower()
            if operation == 'e':
                result = vernam_cipher_encrypt(text, key)
            else:
                result = vernam_cipher_decrypt(text, key)

        elif choice == '2':  # Caesar Cipher
            key = select_key("Caesar")
            operation = input("Encrypt or Decrypt? (e/d): ").lower()
            if operation == 'e':
                result = caesar_cipher_encrypt(text, key)
            else:
                result = caesar_cipher_decrypt(text, key)

        elif choice == '3':  # Transposition Cipher
            key = select_key("Transposition")
            operation = input("Encrypt or Decrypt? (e/d): ").lower()
            if operation == 'e':
                result = transposition_cipher_encrypt(text, key)
            else:
                result = transposition_cipher_decrypt(text, key)

        elif choice == '4':  # Stream Cipher
            key = select_key("Stream")
            operation = input("Encrypt or Decrypt? (e/d): ").lower()
            if operation == 'e':
                result = stream_cipher_encrypt(text, key)
            else:
                result = stream_cipher_decrypt(text, key)

        elif choice == '5':  # Block Cipher
            key = select_key("Block")
            operation = input("Encrypt or Decrypt? (e/d): ").lower()
            if operation == 'e':
                result = block_cipher_encrypt(text, key)
            else:
                result = block_cipher_decrypt(text, key)

        else:
            print("Invalid choice, please try again.")
            continue

        print(f"\nResult: {result}")

if __name__ == "__main__":
    cipher_menu()
