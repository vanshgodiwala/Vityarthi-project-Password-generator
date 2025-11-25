# Password Generator Project

## Overview
This project is a Python-based password generator that creates secure passwords based on user-defined criteria such as length, inclusion of special characters, and exclusion of confusing characters. It also avoids banned words like the user's name and birthday to enhance security.

## Features
- Generates passwords with a mix of uppercase, lowercase, digits, and optionally special characters.
- Option to remove confusing characters such as 0, O, 1, l, and I.
- Checks the strength of generated passwords and classifies them as Strong, Medium, or Weak.
- Prevents inclusion of user-specified banned words in generated passwords.
- Copies the generated password to the clipboard automatically using the `pyperclip` module.
- Saves the latest password locally and logs all generated passwords with timestamps in a history file.
- Option to export the generated password to a timestamped standalone file.

## Usage
Run the Python script `Password-generator.py`. You will be prompted to enter:
- Desired password length (minimum 4 characters).
- Whether to include special characters.
- Whether to remove confusing characters.
- Your name and birthday to exclude from the password.
The generated password will be displayed, copied to your clipboard, saved locally, logged, and optionally exported.

## Requirements
- Python 3.x
- `pyperclip` module for clipboard operations

## Installation
Install dependencies via pip if needed:


pip install pyperclip

## Notes
- Password length should be at least 4 characters for meaningful security.
- Exported password files are saved with a timestamp for uniqueness.

---

This project ensures the creation of strong and customized passwords while maintaining a history for reference and providing convenient clipboard copying.
