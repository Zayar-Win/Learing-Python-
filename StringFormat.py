# str.format() = option method that give users more controable
#                 when displaying string

animal = 'Dog'
thing = 'River'

print("The {} is jumped over the {}".format(animal, thing))
print("The {1} is jumped over the {0}".format(
    thing, animal))  # positional argument
print("The {animal} is jumped over the {thing}".format(
    animal='Cow', thing="moon"))  # keyword arguments
print('My name is {:10}.Nice to meet you'.format('zayarwin'))  # padding right
print('My name is {:>10}.Nice to meet you'.format('zayarwin'))  # padding left
print('My name is {:^10}.Nice to meet you'.format(
    'zayarwin'))  # padding center


number = 1000
print("The number is {:.3f}".format(number))  # wills how three dicimal number
print("The number is {:,}".format(number))  # will use corma for every thousand
print("The number is {:b}".format(number))  # will show number as binary
print("The number is {:o}".format(number))  # will show number as octal
print("The number is {:X}".format(number))  # will show number as hexica
# will show number as sciencific notation
print("The number is {:e}".format(number))
