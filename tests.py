input_word = '''
    Hello world! My name is Valentine!)
    А теперь к тексту%:
    '''


symbols = []
index = 0

while index < len(input_word):
    symbols.append(input_word[index])
    index += 1

print(symbols)

a = [ord(d) for d in symbols]
print(a)