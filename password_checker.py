import re

def password_strength(password):
    """
    Assesses the strength of a password.

    Args:
        password (str): The password to be analyzed.

    Returns:
        str: A strength rating (weak, medium, strong).
    """

    if len(password) < 8:
        return "Weak"

    if not re.search("[a-z]", password):
        return "Weak"
    if not re.search("[A-Z]", password):
        return "Weak"
    if not re.search("[0-9]", password):
        return "Weak"
    if not re.search("[^a-zA-Z0-9]", password):
        return "Weak"

    return "Strong"

# User input
password = input("Enter your password: ")

strength = password_strength(password)
print("Password strength:", strength)

if strength == "Weak":
    print("Suggestion: Use a combination of uppercase, lowercase, numbers, and special characters.")