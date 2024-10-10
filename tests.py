# input_word = '''
#     Hello world! My name is Valentine!)
#     А теперь к тексту%:
#     '''

input_word = input("Введите текст: ")

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



print(cut_data(input_word))
print(data_ord)
print(data_ord_unicode_format)
print(data_for_unicode)