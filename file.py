# reading a file
try:
    with open('text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')

# writing a file
text = "This is new text to file"
try:
    with open('text.txt', 'a') as file:
        file.write(text)
except FileExistsError:
    print('File not found :(')
