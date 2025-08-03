# Random Password Generator

A GUI-based random password generator built using Python and Tkinter. This tool allows users to generate secure passwords of varying strengths and lengths, copy them to the clipboard, and save them with timestamps for future reference.

---

## Features

- Generate random passwords of custom length (8–32 characters)
- Select password strength:
  - Low (lowercase only)
  - Medium (mixed letters)
  - Strong (letters, digits, symbols)
- Copy password to clipboard with a single click
- Save generated passwords with timestamps to a local file (`password_log.txt`)
- Demonstrates password hashing (SHA-256) and secure token generation

---

## Tech Stack

- **Python 3**
- **Tkinter** (for GUI)
- `random`, `string`, `pyperclip`, `secrets`, `hashlib`, `datetime`

---

## Installation

1. Clone this repo or download the Python file:
   ```bash
   git clone https://github.com/your-username/password-generator.git
