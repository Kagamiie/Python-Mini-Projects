# PySharp

This is a simple password manager that allows you mainly to encrypt and decrypt passwords using a key. <br>
It also provides a feature to view all the passwords that have been saved. <br>
At the moment, this script is in **French**, I'll soon done an **English** version.

***Please***: note that this code is provided as an educational example only, this code may changed in the futur to be more secured, but it doesn't mean that you're safe using it. This project should not be used for any personal or professional purposes. This is because the code is not designed with security in mind and could be easily cracked by an attacker. Additionally, as an open source project, it may have vulnerabilities that have not yet been discovered or fixed. Therefore, it is recommended that you use a secure, trusted encryption library for any sensitive data or communication.

## Installation

This tool does not require any installation. Simply download the `password.py` file and run it using Python.
<br>

# Usage
## Encrypting a Message
To encrypt a message, follow these steps:

- Run the `password.py` file using Python.
- When prompted, choose "Chiffrer" (1) option.
- Enter a title for your message (e.g. "Gmail password").
- Enter the message that you want to encrypt.
- The tool will output the encrypted message, which you can copy and save.

## Decrypting a Message
To decrypt a message, follow these steps:

- Run the `password.py` file using Python.
- When prompted, choose the "Déchiffrer" (2) option.
- Enter the encrypted message that you want to decrypt.
- The tool will output the decrypted message.


## Viewing Encrypted Messages
To view a list of encrypted messages, follow these steps:

- Run the `password.py` file using Python.
- When prompted, choose the "Afficher mots de passe" (3) option.
- The tool will display a list of all encrypted messages that have been saved.


## Quitting the Tool
To quit the tool, simply choose the "Quitter" (4) option when prompted.
<br><br>

# Algorithm
This tool uses a custom encryption algorithm that is based on XOR and offset operations. The key is a string of characters that is used to generate a list of integers. Each character in the message is then XORed with a key character and multiplied by the position of the character in the message. Finally, an offset value is XORed with the result to produce the encrypted character.

Decryption is the reverse process of encryption, where each encrypted character is XORed with the offset value, divided by the position of the character, and then XORed with the key character to produce the original character.

# License
This tool is released under the MIT License. See [LICENSE](https://github.com/Kagamiie/Python-Mini-Projects/blob/afe6d60762ad3e834578d1998c144c06be8ce26d/LICENSE) file for details.

# Contributing
Contributions are welcome! If you find any issues or have any suggestions for improvements, please submit a pull request or open an issue.

<br>
