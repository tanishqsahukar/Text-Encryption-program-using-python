import string
import random

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#encrypted message

plain_text = input("enter the message to encrypt: ")
chiper_text = ""

for letters in plain_text:
    index = chars.index(letters)
    chiper_text += key[index]

print(f"orignal message: {plain_text}")
print(f"encrypted message: {chiper_text}")

#decrypted message

plain_text = input("enter the message to decrypt: ")
chiper_text = ""

for letters in plain_text:
    index = key.index(letters)
    chiper_text += chars[index]

print(f"orignal message: {chiper_text}")
print(f"encrypted message: {plain_text}")