import time
print("|---------------------------------------------|")
print("| Hello Friends, Welcome to TicTacToe Game!!! |")
print("| -------------Let's Start!!!!--------------- |")
print("|---------------------------------------------|")
time.sleep(0.8)
print('\nGame is loading ...\n')
time.sleep(0.8)


player_1= [input("Player 1 enter your name: "), "X"]
player_2 = [input("Player 2 enter your name: "), "O"]

player_1_status = True
player_2_status = False
game_status = 'playing'
used_numbers = []

table = []

