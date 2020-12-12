import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    #get user input
    while len(word_letters) > 0:
        #letters used 
        print("you have used these letters: ',' ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = (letter if letter in used_letters else '-' for letter in word)
        print('current word: ', ''.join(word_list))

used_letter = input('guess a letter: ').upper()
if used_letter in alphabet - used_letters:
    used_letters.add(user_letter)
    if user_letter in word_letters:
        word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('you have already used that character. Please try again. ')

        

