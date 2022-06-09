import SUM_IT_UP
import os

HANGMAN = (
"""
  Chance:6
  ----
  |   |
  |
  |
  |
  |
  |
------
""",
"""
  Chance:5
  ----
  |   |
  | (0
  |
  |
  |
  |
------
""",
"""
  Chance:4
  ----
  |   |
  | (0 0)
  |
  |
  |
  |
------
""",
"""
  Chance:3
  ----
  |   |
  | (0 0)
  | ( o )
  |
  |
  |
------
""",
"""
  Chance:2
  ----
  |   |
  | (0 0)
  | ( o )
  | |   |
  |
  |
------
""",
"""
  Chance:1
  ----
  |   |
  | (0 0)
  | ( o )
  | |---|
  |
  |
------
""",
"""
  Chance:0
  ----
  |   |
  | (0 0)
  | ( o )
  | |---|
  |  | |
  |
------
"""
)

def start(f_team):
  os.system('cls')
  fin = open("hangman_word_list.txt","r")                       #read file
  myfile = fin.readlines()
  fin.close()
  word_list = list()                                            #list
  for word in myfile:
      word_list.append(word.strip())

  import random                                                 #modules
  rng = random.Random()
  word_random = rng.sample(word_list,2)

  print("Welcome to HANGMAN competition!!!")
  for team in f_team:
    print(team.team_name, "\nGet ready!!!")
    team.score = 0
    for i in range(2):                                            #for loop
        word_random = rng.choice(word_list)
        maximum_false = len(HANGMAN)
        until_now = "-" * len(word_random)
        false = 0
        used = []
        print("1,2,3,go!!!")

        while false < maximum_false and until_now != word_random: #while loop

            guess = input("Enter your guess: ")
            used.append(guess)

            if guess in word_random:                               #if else
                new_word = ""
                for i in range(len(word_random)):
                    if guess == word_random[i]:
                        new_word += guess
                    elif guess != word_random[i]:
                        new_word += until_now[i]
                until_now = new_word

            else:
                print("your guess, ",guess ,"is wrong (0_0!)")
                print(HANGMAN[false])
                false+=1

            print ("You've used the following letters: \n", used)
            print ("The word so far guessed is : ", until_now)

        if false == maximum_false:
            print("No chance left! 😥")
            print("The word is",word_random)
            team.score+=0
            print("Score :",team.score)

        else:
            print("Success! 😎")
            print("Correct! It is ", word_random)
            team.score+=5
            print("Score :",team.score)
  input("Next game? (Press ENTER)")
  next_game(f_team)

def next_game(f_team):
  SUM_IT_UP.SUM_IT_UP(f_team)

