# Password Generator - Python

## Project Overview

The **Password Generator** is a Python-based command-line application that generates secure, randomized passwords based on user-defined requirements. Users can specify the number of letters, numbers, and special characters to include, and the program generates a strong password by randomly selecting and shuffling the characters.

This project demonstrates the use of Python's built-in libraries for randomization and string manipulation while reinforcing programming fundamentals such as loops, lists, user input handling, and algorithm design.

---

## Objectives

* Generate secure and customizable passwords.
* Allow users to define the number of letters, numbers, and symbols.
* Randomize character positions to enhance password security.
* Demonstrate the use of Python's `random` and `string` modules.
* Strengthen problem-solving and programming skills through a practical application.

---

## Technologies Used

* Python 3
* Python Standard Library

  * `random`
  * `string`

---

## Features

* User-defined password length.
* Customizable number of letters, digits, and special characters.
* Random character selection.
* Randomized character order using `random.shuffle()`.
* Generates a unique password each time the program is executed.
* Simple and interactive command-line interface.

---

## Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── README.md
```

---

## How It Works

1. The program prompts the user to enter:

   * Number of letters
   * Number of symbols
   * Number of numbers
2. Random characters are selected from predefined character sets.
3. The selected characters are stored in a list.
4. The list is shuffled to randomize the character order.
5. The shuffled characters are combined into a single password.
6. The generated password is displayed to the user.

---

## Workflow

```text
Start
   │
   ▼
Enter Number of Letters
   │
   ▼
Enter Number of Symbols
   │
   ▼
Enter Number of Numbers
   │
   ▼
Generate Random Characters
   │
   ▼
Shuffle Characters
   │
   ▼
Create Password
   │
   ▼
Display Password
   │
   ▼
End
```

---

## Sample Execution

```text
Welcome to the PyPassword Generator

How many letters would you like in your password?
8

How many symbols would you like?
3

How many numbers would you like?
4

Generated Password:
A7#mP2@qL5!x9Rt
```

---

## Skills Demonstrated

* Python Programming
* Randomization Techniques
* String Manipulation
* List Operations
* User Input Handling
* Algorithm Design
* Command-Line Application Development
* Problem Solving

---

## Key Concepts Used

* `random.choice()`
* `random.shuffle()`
* `string.ascii_letters`
* `string.digits`
* Lists
* Loops
* User Input
* String Joining

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Vemuriharika/Password-Generator.git
```

### Navigate to the Project Directory

```bash
cd Password-Generator
```

### Run the Program

```bash
python password_generator.py
```

---

## Learning Outcomes

This project helped strengthen my understanding of:

* Python standard libraries.
* Random data generation.
* Password generation logic.
* List manipulation and shuffling.
* Building interactive command-line applications.
* Writing clean and efficient Python code.

---

## Future Enhancements

* Allow users to specify the total password length.
* Include an option to exclude ambiguous characters (e.g., `0`, `O`, `l`, `I`).
* Add password strength analysis.
* Enable password copying directly to the clipboard.
* Save generated passwords securely to a file or password manager.
* Develop a graphical user interface (GUI) using Tkinter.
* Package the application as a standalone executable.

---


## Acknowledgements

This project was developed as part of my Python programming practice to strengthen my understanding of randomization, algorithm design, and secure password generation. It serves as a foundational project for learning user input handling, list manipulation, and the practical use of Python's standard libraries.
