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

while True:
    print_board()
    # strip untuk menghilangkan karakter spasi
    choice = int(input("Enter your move (1 -9) : ").strip())
    # - 1 untuk dapatkan hasil sesuai index array
    # boards[choice - 1] = "X"
    # Pengecekan jika board tsb sdh terisi keluarkan alert jika tidak tandai dgn X
    if boards[choice -1] == " ":
        boards[choice -1] = "X"
    else:
        print("That space is taken")