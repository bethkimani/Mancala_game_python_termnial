while playing:
        display_board()
        if playerOne:
            message = "Player One's turn (Human)..."
            print(message)
            userInput = input("Enter a letter (a-f) to choose a bin or 'q' to Quit: ")
            if userInput == 'q':
                playing = False
                continue
            chosenBin = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0}.get(userInput, -2)
        else:
            message = "Player Two's turn (Computer)..."
            print(message)
            chosenBin = get_computer_move()
            if chosenBin == -1:
                print("No valid moves for the computer. Skipping turn.")
                playerOne = not playerOne
                continue

        if chosenBin == -2:
            print("Invalid input. Try again.")
            continue
        
        lastRecipient = distribute_stones(chosenBin, playerOne)
        if lastRecipient == -1:
            print("You must choose a non-empty bin.")
            continue

        if check_game_over():
            playing = False
            if playerOne:
                binAmount[6] += sum(binAmount[0:6])
                for k in range(6):
                    binAmount[k] = 0
            else:
                binAmount[13] += sum(binAmount[7:13])
                for k in range(7, 13):
                    binAmount[k] = 0

            display_board()
            print("The game is over!")
            if binAmount[13] > binAmount[6]:
                print("Player Two has won the game!")
            elif binAmount[6] > binAmount[13]:
                print("Player One has won the game!")
            else:
                print("The game ended in a tie!")
        else:
            playerOne = not playerOne  # Switch players

if _name_ == "_main_":
    main()