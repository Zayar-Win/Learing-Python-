def hello(name, age, position):
    print('hello ' + name)
    print('age' + '-->', age)
    print('Working as ', position)


hello('zayarwin', 20, "Developer")
# keywords arguments
print('--------------------------')
print('Using keywords arguments')
print('--------------------------')
hello(name='zayarwin', position='Developer', age=20)
