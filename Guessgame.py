# word = "abrakadabra"
# x = word.count("a")
# print(x)

# text = 'X-DSPAM-Confidence:0.8475'

# Find the position of the colon
# colon_pos = text.find(':')

# Slice the string after the colon
# number_str = text[colon_pos + 1:]   # +1 to skip the colon itself

# Convert to float
# number = float(number_str)

# print(number)




# text = "   Hello, Python!   "
# print("Before strip:", repr(text))
# print("After strip:", repr(text.strip()))

# sentence = "I like Java Language so much that it leaves me stunned sometimes, it is so easily understandable." \
# "fast easy to use and what not ,it is best programming language in the world"
# new_sen = sentence.replace("it","Java")
# print(new_sen)


# import math
# deg = float(input())
# rad = math.radians(deg)
# print(f"{deg} degrees = {rad} radians")


# import sys

# while True:
#     print('Type exit to exit.')
#     response = input('>')
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# I am thinking of a number between 1 and 20.
# Take a guess.
# >10
# Your guess is too low.
# Take a guess.
# >15
# Your guess is too low.
# Take a guess.
# >17
# Your guess is too high.
# Take a guess.
# >16
# Good job! You got it in 4 guesses!



import random
secret_number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100.you have only 6 chances so be careful')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))


