import random

words = ['science', 'geography', 'physics', 'geeks']
word = random.choice(words)
spaces = '-' * len(word)

print(spaces)

turns = len(word)

for i in range(turns):
    guess = input("Guess a letter: ")
    if guess in word:
        for j in range(len(word)):
            if word[j] == guess:
                spaces = spaces[:j] + guess + spaces[j+1:]
        print(spaces)
    else:
        print("Sorry, the letter you guessed is not in the word.")
    
    if '-' not in spaces:
        print("Congratulations! You won!")
        break
    
    print("You have {} turns left.".format(turns - i - 1))
    print()

print("Game over. The word was: {}".format(word))

    
        
        


