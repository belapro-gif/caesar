def shift_letter(letter, shift):
    if letter.isalpha():
        base = ord("A") if letter.isupper() else ord("a")
        return chr((ord(letter) - base + shift) % 26 + base)
    return letter # keep non-letter characters unchanged


def caesar_cipher(text, shift):
    encrypted_text = "".join(shift_letter(char, shift) for char in text)
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def run_cipher():
    text = input("Enter your message: ").strip()
    if not text:
        print("Error: Message cannot be empty.")
        return
    
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Error: shift value must be a number.")
        return
    
    shift = shift % 26 #normalize large shifts

    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == "e":
        print("Encrypted message:", caesar_cipher(text, shift))
    elif choice == "d":
        print("Decrypted message:", caesar_decipher(text, shift))
    else:
        print("Invalid choice, Please enter 'e' or 'd'.")


run_cipher()
