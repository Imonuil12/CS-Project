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

table = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def display_table();
    print("\n")
    for i in table:
        print("-------------")
        for j in i:
            print('| ', end="")
            print(j, end="")
            print("|", end="\n")
            print("---------------")
            print("\n")
            
              
            
