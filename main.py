# While Loops in Python

# On variables
nums = list(range(1, 100))

while len(nums) > 0:
    print(nums.pop()) #pop() will stop the while-Look

# On function

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input('Enter a number guess: ')
    
        if guess == '42':
            print('Winner!')
            return False
        else:
            print(f'Try again, isn´t {guess}\n')

guessing_game()

# Using import

from collections import Counter

# 1 example

list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))

dog_house = ['tim', 'bob', 'gim', 'sam']
print(Counter(dog_house))

# 2 example
listThing = [1, 2, 3, "hello", 5]

def loop_using_while(listArg):
    
    counter = 0
    while counter < len(listArg):
        print(listArg[counter])
        counter += 1
         
loop_using_while(listThing)

# 3 example
def loop_using_while():
    dog_house = ['tim', 'bob', 'gim', 'sam']
    counter = 0
    while counter < 4:
        print(dog_house[counter])
        counter += 1
    return [dog_house, counter]

loop_using_while()



    