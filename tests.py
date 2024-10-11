import random
from random import randint

# input_word = input("Введите текст: ")
input_word = '''
    Hello world! My name is Valentine!)
    А теперь к тексту%:
    '''

def text_to_unicode_format(data):
    return ''.join(f'\\u{ord(char):04x}' for char in data)

def cut_data(data):
    symbols = [symbol for symbol in data]
    return symbols


data_ord = [ord(d) for d in cut_data(input_word)]
data_ord_unicode_format = ''.join(f'\\u{ord(d):04x}' for d in cut_data(input_word))
data_for_unicode = [f'\\u{ord(d):04x}' for d in cut_data(input_word)]



print(cut_data(input_word))
print(data_ord)
print(data_ord_unicode_format)
print(data_for_unicode)


def xor_encrypt(data, key_xor):
    encrypted = []
    for char in data:
        encrypted_char = ord(char) ^ key_xor
        encrypted.append(f"\\u{encrypted_char:04x}")
    return ''.join(encrypted)

def xor_decrypt(encrypted_text, key_xor):
    decrypted = []
    for i in range(0, len(encrypted_text), 6):
        hex_value = encrypted_text[i+2:i+6]
        decrypted_char = chr(int(hex_value, 16) ^ key_xor)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

def decode_unicode_escape(data):
    return data.encode().decode('unicode_escape')


key = randint(1, 256)
print(key)

print(f'Soure text: {input_word}')
print(input_word.encode('utf-8'))
encrypted = xor_encrypt(input_word, key)
print('Encrypted:', encrypted)
print(f'Encrypted text: {decode_unicode_escape(encrypted)}')
decrypted = xor_decrypt(encrypted, key)
print('Decrypted:', decrypted)



def xor_encrypt_decrypt(input_bytes, key_xor):
    return bytes([b ^ key_xor for b in input_bytes])


text = "Hello world! Меня зовут Валентин!"
byte_text = text.encode('utf-8')  # Кодируем текст в байты

# key = random.randint(0, 255)

encrypted = xor_encrypt_decrypt(byte_text, key)
print("Зашифрованный текст:", encrypted)

decrypted = xor_encrypt_decrypt(encrypted, key)
decoded_text = decrypted.decode('utf-8')
print("Дешифрованный текст:", decoded_text)


print('\n\n\n', cut_data(input_word))