import string

isRunning = True

# Function for user input
def main():
    global isRunning
    while isRunning:
        user_input = input("Enter A Password: ")
        if password_isValid(user_input):  # Return a bool
            print(f"Password: ( {user_input} ) is valid")
            print(f"Here is the encrypted version: {encrypt_password(user_input)}")  # Pass password and return a string
            isRunning = False
        else:
            print("Password is invalid, please try again")

# Function for validating the password
def password_isValid(password):
    # Password length must be at least 8 characters
    if len(password) < 8:
        print("Password cannot be less than 8 characters.")
        return False
    
    # Password must have letters a-z, A-Z, 0-9, special symbols
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not (has_lower and has_upper and has_digit and has_special):
        print("Password needs to have a combination of letters, numbers, and symbols.")
        return False
    
    # Check for whitespaces
    if any(c.isspace() for c in password):
        print("Password cannot have whitespaces.")
        return False
    
    return True

# Function for encrypting the password using a simple Caesar Cipher
def encrypt_password(password, shift=3):
    encrypted_password = []
    for char in password:
        if char.islower():
            encrypted_password.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif char.isupper():
            encrypted_password.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.isdigit():
            encrypted_password.append(chr((ord(char) - ord('0') + shift) % 10 + ord('0')))
        else:
            # For punctuation and other characters, shift within the ASCII printable range
            encrypted_password.append(chr((ord(char) - 32 + shift) % 95 + 32))
    return ''.join(encrypted_password)

# Run the main function
main()
# ord()returns the decimal value of the ascii character
# % 26 and % 10 -> makes sure that the shifting of the character is wihtin their range
# + ord('a') converts the position to the normal ascii value that is in range of a,A, or 0