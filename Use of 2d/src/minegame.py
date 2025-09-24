def changing_data(p1,p2,bomb_grid,Grid):
    guessing_grid_row = input("please select row to guess")
    guessing_grid_column = input("please select column to guess")
    if Grid[int(guessing_grid_row)-1][int(guessing_grid_column)-1] == 'x':
        print("The grid has already been guessed")
    Grid[int(guessing_grid_row)-1][int(guessing_grid_column)-1] = 'x'
    bomb_grid[int(guessing_grid_row)-1][int(guessing_grid_column)-1] = 'x'
    for i in Grid:
        print(i)
    for i in bomb_grid:
        print(i)
    check_bomb(p1,p2,bomb_grid,Grid)

def check_bomb(p1,p2,bomb_grid,Grid):
    if Grid == bomb_grid and p1 == True:
        print("p1 lost")
    elif Grid == bomb_grid and p2 == True:
        print("p2 lost")
    else:
        if p1 == True:
            p2 = True
            p1 = False
            changing_data(p1,p2,bomb_grid,Grid)
        elif p2 == True:
            p1 = True
            p2 = False
            changing_data(p1,p2,bomb_grid,Grid)
