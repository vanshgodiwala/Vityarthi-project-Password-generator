Password Generator – Full Feature Version

This program is an advanced password generator with multiple security
and usability features.

Features

-   User‑defined password length
-   Option to include/exclude special characters
-   Option to remove confusing characters (0, O, 1, l, I)
-   Blocks username and birthday from appearing in the password
-   Automatic strength rating (0–100)
-   Clipboard auto-copy
-   Password history logging
-   Save latest password locally
-   Export password to timestamped files

Files Created

-   password_history.txt – every generated password with timestamps
-   saved_password.txt – stores the most recent password
-   exported_password_YYYYMMDD_HHMMSS.txt – exported password files

Requirements

Install required library:

    pip install pyperclip

How to Use

1.  Run the script.
2.  Enter desired password length.
3.  Choose whether to include special characters.
4.  Choose whether to remove confusing characters.
5.  Enter a username and birthday to avoid inside the password.
6.  Generated password will:
    -   Display strength score
    -   Be copied to clipboard
    -   Be saved locally
    -   Be added to history log
    -   Optionally be exported

Notes

-   Ensure this program runs in a secure environment.
-   Password files are not encrypted; enable encryption if storing
    sensitive passwords.
