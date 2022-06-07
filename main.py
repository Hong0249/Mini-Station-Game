import hangman, register
import os
f_team = []

def main():
    print("Welcome to the game!")
    print("Type 'H' for help")
    print("Type 'R' before start the game")
    print("##Please create team's name and players' name in namelist.txt before start the game")


    prompt = input()
    while(prompt != "Q"):
        prompt = input("Please enter your command: ")
        if prompt == "H":
            os.system("help.txt")
        elif prompt == "DONE":
            hangman.start(f_team)
        elif prompt == "R":
            print("Save the txt file and close it (●'◡'●)")
            os.system("namelist.txt")
            prompt = input("Press ENTER after finish player registration: ")
            f_team = register.process_namelist()

    exit()

main()