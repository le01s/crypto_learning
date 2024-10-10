def xor_cipher(text, key):
    encrypted_text = ''.join(chr(ord(char) ^ int(key/2)) for char in text)
    return encrypted_text

def xor_decipher(encrypted_text, key):
    return xor_cipher(encrypted_text, key)

user_text = input("Введите текст: ")
key = int(input("Введите числовой ключ (0-255): "))

encrypted = xor_cipher(user_text, key)
print("Зашифрованный текст:", encrypted)

decrypted = xor_decipher(encrypted, key)
print("Расшифрованный текст:", decrypted)

