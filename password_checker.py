import re

# Function to check password strength
def pass_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*()_+{}:"<>?]', password):  # Note: Single '&' in the regex
        score += 1
    
    # Return the password strength based on the score
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

# Get user input
password = input("Enter a password: ")
strength = pass_strength(password)

print(f"-Password strength: {strength}")
if strength != "Strong":
    
    # Suggest making the password at least 8 characters long
    if len(password) < 8:
        print(" - Password should be at least 8 characters long.")
 
    # Suggest adding at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        print(" - Password should contain at least 1 uppercase letter.")
    
    # Suggest adding at least one lowercase letter
    if not re.search(r'[a-z]', password):
        print(" - Password should contain at least 1 lowercase letter.")
    
    # Suggest adding at least one digit
    if not re.search(r'\d', password):
        print(" - Password should contain at least 1 digit.")
    
    # Suggest adding at least one special character
    if not re.search(r'[!@#$%^&*()_+{}:"<>?]', password):
        print(" - Password should contain at least 1 special character.")
