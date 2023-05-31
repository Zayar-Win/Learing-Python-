phone_number = '123-456-789'

for i in phone_number:
    if i == '-':
        continue
    print(i, end="")

for i in range(20):
    if i == 10:
        pass
    else:
        print(i)
