import random
import string

letters = (" eaibodfghjmnpqrtuvw") #Bot uses logic by having most common letters go first in a string, and letters that aren't used in phrases are excluded
guessletters = random.choice(letters)
phrases = ["have fun", "grow up", "fair enough", "quiet down", "great job"]
randomphrase = phrases [random.randint(0, 5)]
blanks = "_"*len(randomphrase)
guessing = True
attempts = 0
guess = ''
lettersguessed = []
print("\nWelcome to Wheel of Fortune")
input("Press enter to make bot start\n")
print('The word contains', len(randomphrase), 'letters and one space.')
print(len(randomphrase) * '_')
input("Press enter to make bot start\n")

while guessing:
    print('Bot has to guess', randomphrase)
    for guess in randomphrase:
        
        if guessletters in randomphrase:
            index = randomphrase.find(guessletters)
            blanks = blanks[:index] + guessletters + blanks[index+1:]
            print("Bot has correctly guessed",guessletters)
            print(blanks)
            guessletters = random.choice(letters)
            input("Press enter to make bot continue\n")  

        if guessletters not in randomphrase:
            index = randomphrase.find(guessletters)
            attempts = attempts + 1
            print("Bot has guessed",guessletters)
            print("Bot has guessed incorrectly", attempts, "times")
            guessletters = random.choice(letters)
            input("Press enter to make bot continue\n")

        elif guessletters in lettersguessed:
            print ("This letter has been used already!")

    print(blanks)
    if "_" not in blanks:
        print("Bot has Solved It!")
        guessing = False
        found = True
        done = True