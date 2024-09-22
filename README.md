# Password Strength Checker 🔐

This is a simple Python program that checks the strength of a password based on certain criteria such as length, presence of uppercase and lowercase letters, digits, and special characters. It provides color-coded feedback and suggestions to improve the password's strength for better security.

## Features
- Evaluates password strength as **Strong**, **Moderate**, or **Weak**.
- Provides suggestions on how to improve weak or moderate passwords.
- Uses colors and emojis to enhance the user experience in the terminal.

## How It Works
The program checks the following criteria for a password:
1. **Length**: Should be at least 8 characters long.
2. **Uppercase Letters**: Must contain at least one uppercase letter (A-Z).
3. **Lowercase Letters**: Must contain at least one lowercase letter (a-z).
4. **Digits**: Must contain at least one digit (0-9).
5. **Special Characters**: Must contain at least one special character (e.g., `!@#$%^&*()`).

### Password Strength Levels:
- **Strong**: Meets all the criteria.
- **Moderate**: Meets 3 or 4 criteria.
- **Weak**: Meets fewer than 3 criteria.
