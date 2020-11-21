import board as border

print("Zacznijmy grę: ")
player = input("Kto ma zacząć X czy 0: ")

board = border.Board(player.upper())

while (not board.check_if_win()) and (not board.check_if_draw()):
    board.show_board()
    x, y = [int(x) for x in input("Podaj współżędne pola na którym chcesz postawić X bądź 0").split()]
    board.put_to_board(x, y)

board.show_board()
print()
if board.check_if_win():
    if board.get_player() == 'X':
        print('Wygrał 0')
    else:
        print('Wygrał X')
else:
    print('Remis')
