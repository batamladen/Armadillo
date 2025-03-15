# ciphers.py

def caesar_cipher(text, shift=3, mode="encrypt"):
    """
    Encrypts or decrypts text using the Caesar cipher.

    :param text: The input text to process.
    :param shift: The number of positions to shift each character (default is 3).
    :param mode: "encrypt" or "decrypt".
    :return: The processed text.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            shift_amount = shift if mode == "encrypt" else -shift
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

