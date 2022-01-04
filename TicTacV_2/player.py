import random

from move import Move

class Player:

    Player_Marker = "X"
    Computer_Marker = "O"

    def __init__(self, is_human = True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.Player_Marker
        else:
            self._marker = Player.Computer_Marker

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1 - 9): "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter an integer between 1 and 9")
        return move

    def get_computer_move(self):
        random_choice = random.choice(list(range(1,10)))
        move = Move(random_choice)
        print("Computer move (1-9): ", move.value)
        return move

# Testing
player = Player()

print(player._is_human) # True
print(player._marker) # X
player.get_move() # testing 1 and out of range 0

# computer player
computer = Player(False)
move = computer.get_move()
print(move.value)