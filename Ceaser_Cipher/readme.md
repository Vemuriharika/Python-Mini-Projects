# Caesar Cipher - Python

## Project Overview

The **Caesar Cipher** is a command-line encryption and decryption application developed using Python. It implements one of the oldest and most widely recognized cryptographic techniques—the Caesar Cipher, a substitution cipher in which each letter in a message is shifted by a fixed number of positions in the alphabet.

This project enables users to securely **encrypt** and **decrypt** text messages by specifying a shift value. It provides a simple and interactive interface while demonstrating the fundamental concepts of classical cryptography and Python programming.



## Objectives

* Implement the Caesar Cipher encryption algorithm.
* Enable users to encrypt and decrypt text messages.
* Handle uppercase and lowercase alphabetic characters efficiently.
* Preserve spaces, numbers, and special characters during encryption and decryption.
* Strengthen understanding of Python programming fundamentals and cryptographic concepts.



## Technologies Used

* Python 3
* Python Standard Library (`string`)



## Features

* Encrypt plain text using a user-defined shift value.
* Decrypt encrypted messages using the same shift value.
* Interactive command-line interface.
* Supports unlimited shift values through modular arithmetic.
* Preserves spaces, numbers, punctuation, and special characters.
* Input validation for encryption/decryption mode.
* Allows users to perform multiple encryption and decryption operations in a single session.



## Project Structure


Caesar-Cipher/

│

├── caesar_cipher.py

└── readme.md


## How It Works

1. The user selects either **Encode** or **Decode** mode.
2. The user enters the message.
3. The user specifies the shift value.
4. The program shifts each alphabetic character by the specified number of positions.
5. Non-alphabetic characters remain unchanged.
6. The encrypted or decrypted message is displayed.
7. The user can choose to repeat the process or exit the application.



## Algorithm

### Encryption

* Each letter is shifted forward by the specified number of positions.
* If the shift exceeds the alphabet length, the position wraps around using modular arithmetic.

Example:

Plain Text : hello
Shift      : 3
Cipher Text: khoor


### Decryption

* Each letter is shifted backward by the specified number of positions using the same shift value.

Example:


Cipher Text: khoor
Shift      : 3
Plain Text : hello


## Sample Execution


Type 'encode' to encrypt or 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here's the encoded result:
mjqqt btwqi

Type 'yes' if you want to go again. Otherwise, type 'no'.


## Key Concepts Demonstrated

* String Manipulation
* Functions
* Loops
* Conditional Statements
* User Input Validation
* Modular Arithmetic
* Python Standard Library
* Command-Line Application Development
* Basic Cryptography



## Skills Demonstrated

* Python Programming
* Algorithm Design
* Problem Solving
* Control Flow
* Data Processing
* Cryptography Fundamentals
* Input Validation
* Clean Code Practices



## Installation

### Clone the Repository

bash
git clone https://github.com/Vemuriharika/Caesar-Cipher.git


### Navigate to the Project Directory

bash
cd Caesar-Cipher


### Run the Program

bash
python caesar_cipher.py


## Learning Outcomes

This project provided hands-on experience in:

* Implementing a classical encryption algorithm.
* Working with strings and character manipulation.
* Applying modular arithmetic for cyclic shifting.
* Building interactive command-line applications.
* Designing reusable Python functions.
* Validating user input and handling edge cases.



## Future Enhancements

* Support uppercase and lowercase letters independently.
* Add file encryption and decryption.
* Generate random encryption keys.
* Implement additional classical ciphers such as Vigenère and Atbash.
* Develop a graphical user interface (GUI) using Tkinter.
* Package the application as a standalone executable.



## Acknowledgements

This project was developed as part of my Python programming practice to strengthen my understanding of classical encryption techniques, algorithm implementation, and command-line application development. It serves as a foundational project for learning the basics of cryptography and secure communication.
