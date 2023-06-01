# exception = events detected during executing that interrupt the flow of a program

try:  # first try with and encounter with exception go to exception code block and check what exception should enter
    numerator = int(input('Enter a number to divide : '))
    denominator = int(input('Enter a number to divide by : '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print('You can divide by zero. idiot!!!!!')
except ValueError as e:
    print(e)
    print('You can divide by string.')
else:
    print(result)
finally:
    print('This will run always')
