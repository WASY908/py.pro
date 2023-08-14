import random
#from words import words
import string

words="wasy"
def get_valid_world(words):
    word = random.choice(words)
    while '-' in word or ' 'in word:
        word=random.choice(words)
    
    
    return word

def hangman():
    word=get_valid_world(words)
    word_letters=set(word)
    aphabet=set(string.ascii_uppercase)
    used_letters = set()

    lives=6

    #get()user input
    while len(word_letters) >0 and lives>0:
     print("You have",lives,"You have used these letters:" , ' '.join(used_letters))
     word_list=[letter if letter in used_letters else '-' for letter in word]
     print('Currect word' , ' '.join (word_list))

     user_letters=input('Guess a letters :').upper()
     if user_letters in aphabet - used_letters:
        used_letters.add(user_letters)
        if user_letters in word_letters:
            word_letters.remove(user_letters)
        else:
           lives=lives-1
           print('Letter is not in word.')
    
     elif user_letters in used_letters:
        print('You have aready used that character . Please try again')
    
     else:
        print('Invalid character.Please try again.')
    if lives==0:
       print("You die !")
    else:
       print("you guess the word")
   

hangman()

