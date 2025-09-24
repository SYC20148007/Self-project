from operator import truediv
from random import randint
from src.minegame import  check_bomb, changing_data

Grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(Grid[2][2])
bomb_grid = [[1 ,2 ,3 ,4 ],
        [5 ,6 ,7 ,8 ],
        [9 ,10,11,12],
        [13,14,15,16]]
bomb_grid[randint(0,3)][randint(0,3)] = 'x'
p1 = True
p2 = False

#
# def changing_data(p1,p2,bomb_grid,Grid):
#     guessing_grid_row = input("please select row to guess")
#     guessing_grid_column = input("please select column to guess")
#     Grid[int(guessing_grid_row)-1][int(guessing_grid_column)-1] = 'x'
#     bomb_grid[int(guessing_grid_row)-1][int(guessing_grid_column)-1] = 'x'
#     print(Grid)
#     print(bomb_grid)
#     check_bomb(p1,p2)
#
# def check_bomb(p1,p2,bomb_grid,Grid):
#     if Grid == bomb_grid and p1 == True:
#         print("p1 lost")
#     elif Grid == bomb_grid and p2 == True:
#         print("p2 lost")
#     else:
#         if p1 == True:
#             p2 = True
#             p1 = False
#             changing_data(p1,p2,bomb_grid,Grid)
#         elif p2 == True:
#             p1 = True
#             p2 = False
#             changing_data(p1,p2,bomb_grid,Grid)

changing_data(p1,p2,bomb_grid,Grid)
