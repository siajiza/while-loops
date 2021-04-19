# While Loops in Python

# On variables
nums = list(range(1, 100))

while len(nums) > 0:
    print(nums.pop()) #pop() will stop the while-Look


# On function

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()
    
        if guess == '42':
            print('Winner!')
            return False
        else:
            print(f'Try again, isn´t {guess}\n')

guessing_game()




    