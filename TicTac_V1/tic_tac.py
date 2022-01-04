# create 9 board string
boards = [" " for i in range(9)]
# print(boards) # kalau d print hasilnya seperti di gambar tanpa hanya 1 grid

#convert 1 grid board into 3x3 grid
def print_board():
    row1 = "| {} | {} | {} |".format(boards[0], boards[1],boards[2])
    row2 = "| {} | {} | {} |".format(boards[3], boards[4],boards[5])
    row3 = "| {} | {} | {} |".format(boards[6], boards[7],boards[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# print_board() # ketika di panggil fungsinya harusnya grid tsb sdh terbentuk 3X3

#pindahkan choice and move into function player move untuk menentukan posisi
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))


    choice = int(input("Enter your move (1 -9) : ").strip())

    if boards[choice -1] == " ":
        boards[choice -1] = icon
    else:
        print("That space is taken")

# untuk mapping victory
def is_victory(icon):
    if  (boards[0] == icon and boards[1] == icon and boards[2] == icon) or \
        (boards[3] == icon and boards[4] == icon and boards[5] == icon) or \
        (boards[6] == icon and boards[7] == icon and boards[8] == icon) or \
        (boards[0] == icon and boards[3] == icon and boards[6] == icon) or \
        (boards[1] == icon and boards[4] == icon and boards[7] == icon) or \
        (boards[2] == icon and boards[5] == icon and boards[8] == icon) or \
        (boards[0] == icon and boards[4] == icon and boards[8] == icon) or \
        (boards[2] == icon and boards[4] == icon and boards[6] == icon) :
        return True
    else:
        return False


while True:
    print_board()
    # # strip untuk menghilangkan karakter spasi
    # choice = int(input("Enter your move (1 -9) : ").strip())
    # # - 1 untuk dapatkan hasil sesuai index array
    # # boards[choice - 1] = "X"
    # # Pengecekan jika board tsb sdh terisi keluarkan alert jika tidak tandai dgn X
    # if boards[choice -1] == " ":
    #     boards[choice -1] = "X"
    # else:
    #     print("That space is taken")
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins ! Congratulation !")
        break
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O Wins ! Congratulation !")
        break
