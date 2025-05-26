import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character types selected."

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? : ").lower() == 'y'
        use_numbers = input("Include numbers? : ").lower() == 'y'
        use_symbols = input("Include symbols? : ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\nGenerated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")

if __name__ == "__main__":
    main()
