# # While Loops in Python

# # On variables
# nums = list(range(1, 100))

# while len(nums) > 0:
#     print(nums.pop()) #pop() will stop the while-Look


# # On function

# def guessing_game():
#     while True:
#         print('What is your guess?')
#         guess = input('Enter a number guess: ')
    
#         if guess == '42':
#             print('Winner!')
#             return False
#         else:
#             print(f'Try again, isn´t {guess}\n')

# guessing_game()


from collections import Counter
# list1 = ['x','y','z','x','x','x','y', 'z']
# print(Counter(list1))

# dog_house = ['tim', 'bob', 'gim', 'sam']
# print(Counter(dog_house))

def loop_using_while():
    dog_house = ['tim', 'bob', 'gim', 'sam']
    Counter = 0
    while Counter < 10:
        print('In our house live, ')
        Counter += 1
        return [dog_house, Counter]
loop_using_while()







    