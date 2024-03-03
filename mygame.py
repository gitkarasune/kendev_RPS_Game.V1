#Kara@CODE.kendev

import sys
import random

def play_mathsgame():

    playagain = True
    while playagain:
        accept = random.choice("12345678910")
        int_pie = int(accept)

        num = random.choice("12345678910")
        computer = int(num)

        print("\n")
        if computer > int_pie:
            print(str(num) + " is " + "greater than".upper() + " " + str(accept))
        elif computer >= int_pie:
            print(str(num) + " is " + " equal to ".upper() + " " + str(accept))
        else:
            print(str(num) + " Is " + "less than".upper() + " " + str(accept))

        print("\nPlay again ?")   

        if ("y" == computer or int_pie):
            return play_mathsgame()
        else:
            playagain

        playagain = input("\nY for yes or \nQ for Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            playagain
            

        if playagain.lower() == "y":
            return play_mathsgame()
        else:
            print("\n 🥂🥂🥂🥂")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋🏿🙋🏿‍♂️\n\n") 
            
 
play_mathsgame()

# github.com/gitKarasune
# We're selecting the numbers randomly and it's working correctly.
# Dave remains the best TEACHER
