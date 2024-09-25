
# Cipher Suite - Encryption and Decryption Tool

This project provides an interactive Python tool for encrypting and decrypting text using five different cipher techniques:

1. **Vernam Cipher**
2. **Caesar Cipher**
3. **Transposition Cipher**
4. **Stream Cipher**
5. **Block Cipher**

The tool allows users to select a cipher, input text, choose encryption or decryption, and see the result. It also provides pre-configured keys for each cipher and base64 encoding for safe output.

## Features

- **Vernam Cipher**: Encrypts/Decrypts text using a character-wise XOR operation with a key.
- **Caesar Cipher**: Implements a basic Caesar shift cipher, rotating letters based on a provided shift value.
- **Transposition Cipher**: Rearranges the text into a matrix and reads it column-wise for encryption.
- **Stream Cipher**: Uses XOR encryption with a random number generated from a seed.
- **Block Cipher**: Implements a basic ECB (Electronic Codebook) mode, applying a Vernam Cipher on fixed-size blocks.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cipher-suite.git
```

Navigate into the directory:

```bash
cd cipher-suite
```

Install any necessary dependencies (if required):

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python cipher_suite.py
```

### Ciphers

- **Vernam Cipher**: Selects a key from the available options and XORs the input text with the key.
- **Caesar Cipher**: Shifts alphabetic characters by a selected number.
- **Transposition Cipher**: Encrypts by rearranging characters based on the provided key (column number).
- **Stream Cipher**: XORs each character of the input text with a random number based on a seed.
- **Block Cipher**: Splits text into 8-character blocks and applies the Vernam cipher to each block.

### Example Run

```
Select the Encryption/Decryption Technique:
1. Vernam Cipher
2. Caesar Cipher
3. Transposition Cipher
4. Stream Cipher
5. Block Cipher
6. Exit
Enter your choice (1-6): 2

Enter the text to encrypt/decrypt: HelloWorld

Available keys for Caesar Cipher: [3, 5, 7]
Select one key from the above (enter exactly as shown for Vernam/Block or a number for others): 3
Encrypt or Decrypt? (e/d): e

Result: KhoorZruog
```

### Keys

Each cipher provides a set of keys that users can choose from. For example:
- Vernam Cipher: Select a pre-defined string key.
- Caesar Cipher: Select a number for the shift.
- Stream Cipher: Select a seed number for the random generator.
- Block Cipher: Select a string key for block encryption.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Contributions are welcome!

