import random
import string
import pyperclip
import os
from datetime import datetime

HISTORY_FILE = "password_history.txt"   # Stores all passwords generated
SAVE_FILE = "saved_password.txt"        # Saves the latest password


def log_password(password):
    """Appends password with timestamp to history file."""
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{datetime.now()}  ->  {password}\n")


def save_password_locally(password):
    """Saves the latest password to a file (overwrites each time)."""
    with open(SAVE_FILE, "w") as f:
        f.write(password)


def export_password(password):
    """Exports password to a standalone export file."""
    export_name = f"exported_password_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(export_name, "w") as f:
        f.write(password)
    print(f"✔ Password exported to file: {export_name}")


def generate_password(length, use_special, remove_confusing, banned_words):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation if use_special else ""

    confusing_chars = "0O1lI|"

    if remove_confusing:
        upper = ''.join(c for c in upper if c not in confusing_chars)
        lower = ''.join(c for c in lower if c not in confusing_chars)
        digits = ''.join(c for c in digits if c not in confusing_chars)
        special = ''.join(c for c in special if c not in confusing_chars)

    all_chars = upper + lower + digits + special

    if len(all_chars) == 0:
        raise ValueError("Character set is empty! Too many exclusions.")

    # Generating untill no banned words are found
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if not any(word.lower() in password.lower() for word in banned_words if word):
            return password


def check_strength(password, use_special):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password) if use_special else True

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"


# MAIN PROGRAM 

length = int(input("Enter desired password length: "))

use_special = input("Include special characters? (y/n): ").lower() == "y"
remove_confusing = input("Remove confusing characters (0,O,1,l,I)? (y/n): ").lower() == "y"

username = input("Enter your name (to avoid in password): ")
birthday = input("Enter your birthday (to avoid in password): ")

banned_words = [username, birthday]

if length < 4:
    print("Password length must be at least 4.")
else:
    pwd = generate_password(length, use_special, remove_confusing, banned_words)
    strength = check_strength(pwd, use_special)

    print("\nGenerated Password:", pwd)
    print("Password Strength:", strength)

    # Copy to clipboard
    pyperclip.copy(pwd)
    print("✔ Password copied to clipboard!")

    # Saving latest password locally to device 
    save_password_locally(pwd)
    print("✔ Password saved locally!")

    # Log password into history
    log_password(pwd)
    print("✔ Password added to history log!")

    # Export option
    export_choice = input("Export password to a file? (y/n): ").lower()
    if export_choice == "y":
        export_password(pwd)

