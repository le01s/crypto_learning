def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_base = ord('а') if char.islower() else ord('А')
            encrypted_text += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

user_text = input("Введите текст: ")
shift_value = int(input("Введите сдвиг: "))

encrypted = caesar_cipher(user_text, shift_value)
print("Зашифрованный текст:", encrypted)

decrypted = caesar_decipher(encrypted, shift_value)
print("Расшифрованный текст:", decrypted)