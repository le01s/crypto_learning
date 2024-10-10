input_word = '''
    Hello world! My name is Valentine!)
    А теперь к тексту%:
    '''

def text_to_unicode_format(text):
    return ''.join(f'\\u{ord(char):04x}' for char in text)


symbols = []
index = 0

while index < len(input_word):
    symbols.append(input_word[index])
    index += 1



data_ord = [ord(d) for d in symbols]
data_ord_unicode_format = ''.join(f'\\u{ord(d):04x}' for d in symbols)
data_for_unicode = [f'\\u{ord(d):04x}' for d in symbols]



print(symbols)
print(data_ord)
print(data_ord_unicode_format)
print(data_for_unicode)