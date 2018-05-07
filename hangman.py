def hangman(word):
    wrong = 0
    stages = ["",
              "____________          ",
              "|           |         ",
              "|           O         ",
              "|          /|\        ",
              "|          / \        ",
              "|                     "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "_" not in board:
            print("You Win!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:wrong]))
        print("You lose. It was {}.".format(word))

from random import randint

my_words = ["cat", "dog", "boy", "girl"]

hangman(my_words[randint(0,3)])
