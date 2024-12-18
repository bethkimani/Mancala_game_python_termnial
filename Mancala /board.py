# display_board/display_board.py

def display_board():
    print("+----+----+----+----+----+----+----+----+")
    print("|    |" + str(binAmount[12]).rjust(2) + "    |" + str(binAmount[11]).rjust(2) + " |" + str(binAmount[10]).rjust(2) +
          "  | " + str(binAmount[9]).rjust(2) + " |" + str(binAmount[8]).rjust(2) + " | " + str(binAmount[7]).rjust(2) + "   |    |")
    print("|" + str(binAmount[13]).rjust(2) + "   |----+----+----+----+----+-----|" + str(binAmount[6]).rjust(2) + " |")
    print("|    |  " + str(binAmount[0]).rjust(2) + " | " + str(binAmount[1]).rjust(2) + "  | " + str(binAmount[2]).rjust(2) +
          "   | " + str(binAmou


nt[3]).rjust(2) + "  | " + str(binAmount[4]).rjust(2) + " |" + str(binAmount[5]).rjust(2) + "   |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("        f     e     d     c     b     a")
    print("")