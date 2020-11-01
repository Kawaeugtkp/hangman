def hangman(word):
    wrong = 0
    stages = ["1", "2", "3", "4", "5", "6"]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    while wrong < len(stages) - 1:
        m = input("1文字を入力してね:")
        if m in rletters:
            cind = rletters.index(m)
            board[cind] = m
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        print("".join(stages[0:wrong+1]))
        if "__" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break

    if not win:
        print("".join(stages[0:wrong+1]))
        print("Correct is {}".format(word))
