def hangman (word):
    wrong = 0
    stage = ["",
         "_________________             ",
         "｜             ｜         ",
             
         "｜             ◯         ",

         "｜           ／｜＼        ",
             
         "｜             ｜          ",

         "｜           ／  ＼       ",

         "｜                            "

          ]
    rletters = list (word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stage)-1:
        #-1是因为stage的长度为8，多了最上面为了使人看起来更整齐多加了一行空格
        print("\n")
        msg = "guess a letter："
        char = input (msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong+=1
        print((" ".join(board)))
        e = wrong+1
        print("\n".join(stage[0:e]))
        if "_"not in board:
            print ("you win!")
            print (" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stage[0:e]))
        print("you lose!it was {}.".format(word))


hangman("cat")

input()
