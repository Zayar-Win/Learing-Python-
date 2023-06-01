import random

x = random.randint(1, 6)  # this will give us random number between 1 and 6
y = random.random()  # this will give us floating number between 0 and 1

print(x)
print(y)

myLists = ['paper', 'rock', 'scissors']
print(random.choice(myLists))  # this will choise random value of myLists

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']

random.shuffle(cards)  # this will shuffle our cards
print(cards)
