import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Generate a random password with the specified criteria."""
    
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    digit_chars = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special_chars else ""
    
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    
    if not all_chars:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter password length (default 12): ") or "12")
    except ValueError:
        print("Invalid length. Using default length 12.")
        length = 12
    
    use_uppercase = input("Include uppercase letters? (y/n, default y): ").strip().lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").strip().lower() != 'n'
    use_special_chars = input("Include special characters? (y/n, default y): ").strip().lower() != 'n'
    
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
