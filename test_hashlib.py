import hashlib

myHash = input('введите значение: ')
hash_object = hashlib.sha512(myHash.encode())
print(hash_object.hexdigest())