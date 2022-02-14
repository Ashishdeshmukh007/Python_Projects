import random
from Hangman_art_logo import logo, stages
from Hangman_word_list import  word_list


print(logo)
print("\n Welcome To The Hangman Bollywood Movie Guess Game!")
print(" \n Please Save Hangman From Hanging By Guessing Correct Letters Of Bollywood Movie Name! \n")

choosen_word= random.choice(word_list).lower()

dipsplay_list=[]
game_is_finished = False
lives = len(stages) - 1

for char in choosen_word:
    dipsplay_list+="_"

print(dipsplay_list
      )
while not game_is_finished:
    guess_letter = input("Please Guess The Letter From Bollywood Movie \n").lower()

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess_letter:
            dipsplay_list[position] = letter

    if guess_letter not in choosen_word:
        lives-=1
        if lives == 0:
            game_is_finished= True
            print("Opps You Loose Because You Lost All Lives")
            print(f"The correct movie name was {choosen_word}")

    print(stages[lives])
    print(dipsplay_list)


    if "_" not in dipsplay_list:
        game_is_finished = True
        print("Congratulations You Won You Guessed Correct Movie Name")







