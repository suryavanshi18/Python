import random
import string

import words

wrd=words.words
wrd=[w.upper() for w in wrd]
def getValidWords(word):
    randomWord=random.choice(word)
    while '-' in randomWord or ' ' in word:
        randomWord=random.choice(word)
    return randomWord
def hangman():
    word=getValidWords(wrd)
    word_letters=set(word)
    alphabet=set(string .ascii_uppercase)
    used_letters=set()
    lives=6
    while len(word_letters)>0:
        print("You have,",lives,"lives left and you have used these letters ",' '.join(used_letters))
        word_List=[letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ",' '.join(word_List))
        user_letter=input("Guess a letter ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
        elif user_letter in used_letters:
            print("You have already used this letter")
        else:
            print("Invalid character")
    if(lives==0):
        print("You died,the word is,",word)
    print("You have guessed the word",word,"!!")
hangman()


    
