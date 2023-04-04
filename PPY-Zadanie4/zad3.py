def szyfr_cezara(message, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
    key = key % len(alphabet)
    encrypted_message = ''
    for char in message:
        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            new_position = (char_index + key) % len(alphabet)
            encrypted_char = alphabet[new_position]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message