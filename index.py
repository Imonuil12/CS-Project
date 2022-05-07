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

def display_table():
    print("\n")
    for i in table:
        print("-------------")
        for j in i:
            print('| ', end="")
            print(j, end="")
            print("|", end="\n")
            print("---------------")
            print("\n")
            
def check_column():
    
    row_1=[i[0] for i in table]
    row_2=[i[1] for i in table]
    row_3=[i[2] for i in table]
    
    if row_1.count(row_1[0])==3 or row_2.count(row_2[0])==3 or row_3.count(row_3[0])==3:
        return True
    else:
        return False
    
def check_row():
    
    col_1 = table[0]
    col_2 = table[1]
    col_3 = table[2]
    
    if col_1.count(col_1[0])==3 or col_2.count(col_2[0])==3 or col_3.count(col_3[0])==3:
        return True
    else:
        return False



    
            
