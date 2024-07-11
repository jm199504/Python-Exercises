def encrypt_string(input_string, shift):
    """
    Encrypt a string by shifting each character by a given number of positions.

    :param input_string: The string to be encrypted.
    :param shift: The number of positions to shift each character.
    :return: The encrypted string.
    """
    encrypted_string = ""
    for char in input_string:
        if char.isalpha():
            # Determine the base for uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Calculate the shifted character
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_string += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            encrypted_string += char
    return encrypted_string


# Example usage:
original_string = "Hello, World!"
shift_amount = 3
encrypted = encrypt_string(original_string, shift_amount)
print(f"Original: {original_string}")
print(f"Encrypted: {encrypted}")
