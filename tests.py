
from random import randint

# input_word = input("Введите текст: ")
input_word = '''
    Hello world! My name is Valentine!)
    А теперь к тексту%:
    '''
def text_to_unicode_format(text):
    return ''.join(f'\\u{ord(char):04x}' for char in text)

def cut_data(input_word):
    symbols = []
    index = 0
    while index < len(input_word):
        symbols.append(input_word[index])
        index += 1
    return symbols


data_ord = [ord(d) for d in cut_data(input_word)]
data_ord_unicode_format = ''.join(f'\\u{ord(d):04x}' for d in cut_data(input_word))
data_for_unicode = [f'\\u{ord(d):04x}' for d in cut_data(input_word)]
# data_ord_from_unicode = [ord(d) for d in data_for_unicode]



print(cut_data(input_word))
print(data_ord)
print(data_ord_unicode_format)
print(data_for_unicode)


def xor_encrypt(text, key):
    encrypted = []
    for char in text:
        encrypted_char = ord(char) ^ key
        encrypted.append(f"\\u{encrypted_char:04x}")
    return ''.join(encrypted)

def xor_decrypt(encrypted_text, key):
    decrypted = []
    for i in range(0, len(encrypted_text), 6):
        hex_value = encrypted_text[i+2:i+6]
        decrypted_char = chr(int(hex_value, 16) ^ key)
        decrypted.append(decrypted_char)
    return ''.join(decrypted)

def decode_unicode_escape(text):
    return text.encode().decode('unicode_escape')


key = randint(10000, 50000)
print(key)
print(f'Soure text: {input_word}')
encrypted = xor_encrypt(input_word, key)
print('Encrypted:', encrypted)
print(f'Encrypted text: {decode_unicode_escape(encrypted)}')
decrypted = xor_decrypt(encrypted, key)
print('Decrypted:', decrypted)
