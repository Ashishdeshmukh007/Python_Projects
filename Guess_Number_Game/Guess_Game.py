import random

from Logo import logo

print(f"{logo} \n")

print("WELCOME TO THE NUMBER GUESSING GAME \n")

number_list=[]

for i in range(1,101):
    number_list.append(i)

random_choice= random.choice(number_list)

print("I'm thinking of a number between 1 and 100 try to guess the number which i am thinking.")

difficulty= input("Choose the dificulty : Type Easy or Hard ? \n").lower()

end_of_game= False


while not end_of_game:

    if difficulty == "easy":
        lives = 10
        print(f"You have {lives} attempts to guess the number \n")

        for live in range(1,11):
            guess = int(input("Please Make a Guess \n"))

            if guess < random_choice:
                print("Too Low \n")
                lives -= 1

                if lives==0:
                    print("Unfortunatly you lost all your lives and you loose \n")
                    end_of_game=True
                else:
                    print(f"You have only {lives} lives left to guess the number \n")

            elif guess == random_choice:
                print("Congratulations you guessed it right and You Won \n")
                end_of_game = True
                break

            elif guess > random_choice:
                print("Too High \n")
                lives-=1

                if lives == 0:
                    print("Unfortunatly you lost all your lives and you loose \n")
                    end_of_game = True
                else:
                    print(f"You have only {lives} lives left to guess the number \n")



    elif difficulty == "hard":
        lives = 5
        print(f"You have {lives} attempts to guess the number \n")

        for live in range(1,6):
            guess = int(input("Please Make a Guess \n"))

            if guess < random_choice:
                print("Too Low \n")
                lives -= 1

                if lives == 0:
                    print("Unfortunatly you lost all your lives and you loose \n")
                    end_of_game = True
                else:
                    print(f"You have only {lives} lives left to guess the number \n")

            elif guess == random_choice:
                print("Congratulations you guessed it right and You Won \n")
                end_of_game = True
                break

            elif guess > random_choice:
                print("Too High \n")
                lives-=1

                if lives == 0:
                    print("Unfortunatly you lost all your lives and you loose \n")
                    end_of_game = True
                else:
                    print(f"You have only {lives} lives left to guess the number \n")


