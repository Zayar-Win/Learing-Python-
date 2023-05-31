# args = parameters that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# if we use like this we cant pass many arguments we have limitations
def sum(num1, num2):
    sum = num1 + num2
    print(sum)


sum(1, 2)

# if you want to pass arguments without limiation use *args


def sum(*args):
    sum = 0
    args = list(args)  # type casting tuple into list
    for arg in args:
        sum += arg
    print(sum)


sum(1, 2, 3, 4, 5, 6, 7, 8)
