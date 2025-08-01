import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file=="vecna.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key","rb") as thekey:
	secretkey=thekey.read()

for file in files:
    with open(file,"rb") as thefile:
        content= thefile.read()
    content_decrypt=Fernet(secretkey).decrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_decrypt)
        
