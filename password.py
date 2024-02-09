import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
generated_password = generate_password(length=16, use_lowercase=True, use_uppercase=True, use_digits=True, use_punctuation=True)
print("Generated Password:", generated_password)
