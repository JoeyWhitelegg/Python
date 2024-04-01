# to create a hashkey with Python

import hashlib

String = str(input("Type out the word you would like to hash "))
Hash_Type = str(input("Type your preferred hash type. SHA or MD5 "))
if Hash_Type == 'SHA':
    Final_Hash = hashlib.sha256(String.encode()).hexdigest()
    print(Final_Hash)

else:
    Final_Hash = hashlib.md5(String.encode()).hexdigest()
    print(Final_Hash)
