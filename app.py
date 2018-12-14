import random

# all variables
prize_easy = open("prize_easy.txt", "r")
prize_medium = open("prize_medium.txt", "r")
prize_hard = open("prize_hard.txt", "r")
number = 0
guess = 0
tries = 0
try_limit = 3
try_again = "y"
try_again_confirm = ""
win_count = 0
diff_level = ""
won_games = 0
# Difficulty class & objects
class difficulties:
    def __init__(self, name, num, file):
        self.name = name
        self.num = num
        self.file = file

easy = difficulties("easy", 3, prize_easy)
medium = difficulties("medium", 4, prize_medium)
hard = difficulties("hard", 5, prize_hard)

# Functions
def randomize():
    global number
    global diff_level
    global difficulties
    number = random.randrange(1, (globals()[diff_level.lower()].num+1))


def reset_tries():
    global tries
    tries = 0

def reset_wins():
    global win_count
    win_count = 0


# ----------Game Intro--------------
print("\n\n-*-*-*--*-*-*--*-*-*--*-*-*-\n\n"
      "Welcome to the guessing game!\n\n"
      "-*-*-*--*-*-*--*-*-*--*-*-*-\n\n"
      "In this game, your goal is to guess a randomly chosen number 5 times.\n\n"
      "If you achieve this goal, you will get a prize!")

print("Each difficulty level corresponds to a better prize.")


# gameloop

while try_again == "y":
    try_again_confirm = ""

    # choose difficulty loop:
    while str(diff_level) not in ["easy", "medium", "hard"]:
        diff_level = input("\nChoose your difficulty level(Easy, Medium or Hard): ")
        diff_level = diff_level.lower()
        randomize()
        if str(diff_level) not in ["easy", "medium", "hard"]:
            print("try again")
        else:
            break
    # Main game mechanic:
    try:
        # # Diagnostic (and cheating) prints
        # print(number)
        # print(diff_level)
        # print(str(globals()[diff_level.lower()].num))

        print("\n-------------------------------\n",
              "Guesses left: "+str(3-tries),
              "\n-------------------------------\n")

        guess = int(input("Choose a number between 1 and "+str(globals()[diff_level.lower()].num)+": "))
        if guess == number:
            win_count += 1
            if win_count == 5:
                print(globals()[diff_level.lower()].file.read())
                print("\n\nYou win the game!")
                won_games += 1

                # Play again?
                while try_again_confirm not in ["y", "n"]:
                    try_again_confirm = input("Play again? y/n: ")
                    if try_again_confirm == "y":
                        reset_tries()
                        try_again = try_again_confirm
                        diff_level = ""
                        reset_wins()

                    elif try_again_confirm == "n":
                        try_again = try_again_confirm
                        try_again_confirm = ""
                        print("\n-------------------------------\n",
                              "Have a great day, I'll miss you, you're a real winner :)\n",
                              "Total won games: "+str(won_games),
                              "\n-------------------------------\n")

                        print("Press Enter to close:")
                        input()
                        break
                    else:
                        print("Please enter a correct response")

            else:
                print("\n\n-*-*-*--*-*-*--*-*-*--*-*-*-")
                print("You got it!")
                print(str(win_count)+ " right, "+str(5-win_count)+" to go!")
                print("-*-*-*--*-*-*--*-*-*--*-*-*-")
                reset_tries()
                randomize()


        elif guess != number and tries < try_limit-1:
            tries += 1
            print("\n-------------------------------\n",
                  "\nOops! Guess Again")
        else:
            print("You lose\n\n")
            while try_again_confirm not in ["y","n"]:
                try_again_confirm = input("Try again? y/n: ")
                if try_again_confirm == "y":
                    reset_tries()
                    try_again = try_again_confirm
                    reset_wins()
                    randomize()
                    diff_level = ""
                elif try_again_confirm == "n":
                    print("\n\nYou give up too easily. Goodbye!\n"+"Total wins: "+str(won_games))
                    print("Press Enter to close:")
                    try_again = try_again_confirm
                    input()
                else:
                    print("Please enter a correct response")

    except ValueError:
        print("\nPlease guess a number")



