# A program designed to bruteforce a PDF Password if it uses a standard dictionary word (uppercase, lowercase, and capitalized versions are tried)
# Requires the PyPDF2 imported from Pip or into your pycharm project
# Also requires a dictionary file - called dictionary.txt here that breaks it down into an iterable list object
# project comes from Al Sweigart's "Automate the Boring Stuff with Python 2nd Edition - chapter 15)
# project will also print off a count of every thousand words so you know it's working

import PyPDF2

with open('dictionary.txt', 'r') as file:
    content = file.read()
    content_list = content.split("\n")
total = len(content_list)
pdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))
list_count = 0

for word in content_list:
    if pdfReader.decrypt(word.lower()) == 1:
        print(word.lower())
        break
    elif pdfReader.decrypt(word) == 1:
        print(word)
        break
    elif pdfReader.decrypt(word.title()) == 1:
        print(word.title())
        break
    else:
        list_count += 1
        if list_count % 1000 == 0:
            print(list_count)

