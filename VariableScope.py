# scope = The region that a variable is recognized
#         A variable is only available from inside the region that it is created
#         A global and locally scoped version of a variable can be created

name = 'Zayarwin'  # global scope (available inside & outside of functions)


def print_name():
    name = 'Zayar'  # local scope (can only available inside this function)
    print(name)


print(name)
print_name()
