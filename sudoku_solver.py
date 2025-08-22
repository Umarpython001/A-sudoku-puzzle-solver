#SUDOKU SOLVER

from shapes import decorate_time
acceptable = {1,2,3,4,5,6,7,8,9}

test_grid_layout=[
    [0,0,0, 9,0,5, 1,0,0],
    [0,0,8, 0,0,0, 0,0,5],
    [4,0,0, 1,0,0, 0,3,0],

    [0,2,0, 0,9,0, 0,0,0],
    [1,0,0, 4,0,8, 0,0,0],
    [0,0,0, 0,6,0, 0,1,7],

    [2,7,0, 6,1,0, 0,0,0],
    [0,0,0, 0,2,0, 3,0,0],
    [0,6,0, 3,0,0, 4,0,0]
]

def sudoku_solver():
    def display_unsolved_grid(grid = test_grid_layout):
        print("-------UNSOLVED SUDOKU GRID---------")
        print(f"{grid[0][0], grid[0][1], grid[0][2]} | {grid[0][3], grid[0][4], grid[0][5]} | {grid[0][6], grid[0][7], grid[0][8]}")
        print(f"{grid[1][0], grid[1][1], grid[1][2]} | {grid[1][3], grid[1][4], grid[1][5]} | {grid[1][6], grid[1][7], grid[1][8]}")
        print(f"{grid[2][0], grid[2][1], grid[2][2]} | {grid[2][3], grid[2][4], grid[2][5]} | {grid[2][6], grid[2][7], grid[2][8]}")
        print("----------+-----------+-----------")
        print(f"{grid[3][0], grid[3][1], grid[3][2]} | {grid[3][3], grid[3][4], grid[3][5]} | {grid[3][6], grid[3][7], grid[3][8]}")
        print(f"{grid[4][0], grid[4][1], grid[4][2]} | {grid[4][3], grid[4][4], grid[4][5]} | {grid[4][6], grid[4][7], grid[4][8]}")
        print(f"{grid[5][0], grid[5][1], grid[5][2]} | {grid[5][3], grid[5][4], grid[5][5]} | {grid[5][6], grid[5][7], grid[5][8]}")
        print("----------+-----------+-----------")
        print(f"{grid[6][0], grid[6][1], grid[6][2]} | {grid[6][3], grid[6][4], grid[6][5]} | {grid[6][6], grid[6][7], grid[6][8]}")
        print(f"{grid[7][0], grid[7][1], grid[7][2]} | {grid[7][3], grid[7][4], grid[7][5]} | {grid[7][6], grid[7][7], grid[7][8]}")
        print(f"{grid[8][0], grid[8][1], grid[8][2]} | {grid[8][3], grid[8][4], grid[8][5]} | {grid[8][6], grid[8][7], grid[8][8]}")
        print("----------------------------------")




    def find_box_number(row_index, index, grid=test_grid_layout):
        if (row_index==0 and index==0) or (row_index==0 and index==1) or (row_index==0 and index==2) or (row_index==1 and index==0) or (row_index==1 and index==1) or (row_index==1 and index==2) or (row_index==2 and index==0) or (row_index==2 and index==1) or (row_index==2 and index==2):
            return 1
        if (row_index==0 and index==3) or (row_index==0 and index==4) or (row_index==0 and index==5) or (row_index==1 and index==3) or (row_index==1 and index==4) or (row_index==1 and index==5) or (row_index==2 and index==3) or (row_index==2 and index==4) or (row_index==2 and index==5):
            return 2
        if (row_index==0 and index==6) or (row_index==0 and index==7) or (row_index==0 and index==8) or (row_index==1 and index==6) or (row_index==1 and index==7) or (row_index==1 and index==8) or (row_index==2 and index==6) or (row_index==2 and index==7) or (row_index==2 and index==8):
            return 3
        if (row_index==3 and index==0) or (row_index==3 and index==1) or (row_index==3 and index==2) or (row_index==4 and index==0) or (row_index==4 and index==1) or (row_index==4 and index==2) or (row_index==5 and index==0) or (row_index==5 and index==1) or (row_index==5 and index==2):
            return 4
        if (row_index==3 and index==3) or (row_index==3 and index==4) or (row_index==3 and index==5) or (row_index==4 and index==3) or (row_index==4 and index==4) or (row_index==4 and index==5) or (row_index==5 and index==3) or (row_index==5 and index==4) or (row_index==5 and index==5):
            return 5
        if (row_index==3 and index==6) or (row_index==3 and index==7) or (row_index==3 and index==8) or (row_index==4 and index==6) or (row_index==4 and index==7) or (row_index==4 and index==8) or (row_index==5 and index==6) or (row_index==5 and index==7) or (row_index==5 and index==8):
            return 6
        if (row_index==6 and index==0) or (row_index==6 and index==1) or (row_index==6 and index==2) or (row_index==7 and index==0) or (row_index==7 and index==1) or (row_index==7 and index==2) or (row_index==8 and index==0) or (row_index==8 and index==1) or (row_index==8 and index==2):
            return 7
        if (row_index==6 and index==3) or (row_index==6 and index==4) or (row_index==6 and index==5) or (row_index==7 and index==3) or (row_index==7 and index==4) or (row_index==7 and index==5) or (row_index==8 and index==3) or (row_index==8 and index==4) or (row_index==8 and index==5):
            return 8
        if (row_index==6 and index==6) or (row_index==6 and index==7) or (row_index==6 and index==8) or (row_index==7 and index==6) or (row_index==7 and index==7) or (row_index==7 and index==8) or (row_index==8 and index==6) or (row_index==8 and index==7) or (row_index==8 and index==8):
            return 9

    def boxes(grid=test_grid_layout):
        boxes_and_items={

            1:[grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2], ],
            2:[grid[0][3], grid[0][4], grid[0][5], grid[1][3], grid[1][4], grid[1][5], grid[2][3], grid[2][4], grid[2][5], ],
            3:[grid[0][6], grid[0][7], grid[0][8], grid[1][6], grid[1][7], grid[1][8], grid[2][6], grid[2][7], grid[2][8], ],
            4:[grid[3][0], grid[3][1], grid[3][2], grid[4][0], grid[4][1], grid[4][2], grid[5][0], grid[5][1], grid[5][2], ],
            5:[grid[3][3], grid[3][4], grid[3][5], grid[4][3], grid[4][4], grid[4][5], grid[5][3], grid[5][4], grid[5][5], ],
            6:[grid[3][6], grid[3][7], grid[3][8], grid[4][6], grid[4][7], grid[4][8], grid[5][6], grid[5][7], grid[5][8], ],
            7:[grid[6][0], grid[6][1], grid[6][2], grid[7][0], grid[7][1], grid[7][2], grid[8][0], grid[8][1], grid[8][2], ],
            8:[grid[6][3], grid[6][4], grid[6][5], grid[7][3], grid[7][4], grid[7][5], grid[8][3], grid[8][4], grid[8][5], ],
            9:[grid[6][6], grid[6][7], grid[6][8], grid[7][6], grid[7][7], grid[7][8], grid[8][6], grid[8][7], grid[8][8], ]
        }
        return boxes_and_items


    def validate_square(number, row_index, column_index, grid=test_grid_layout):
        box_number = find_box_number(row_index, column_index)
        smth = boxes()
        box_as_list=smth[box_number]
        for i in box_as_list:
            if i==number:
                return False
        return True

    def validate_row(number, row_index, grid = test_grid_layout):
        for counter in grid[row_index]:
            if counter == number:
                return False
        return True

    def validate_other_rows(number , row_index, column_index, grid=test_grid_layout):#takes in the absent number that were trying as first argument the zero index that were trying it in and the row index to tell us the row that were working with
        for horizon in grid:
            if horizon[column_index] == number:
                return False
        return True


    def check_if_valid(number, row_index, column_index):
        check_row = validate_row(number, row_index)
        check_other_rows = validate_other_rows(number, row_index, column_index)
        check_box = validate_square(number, row_index, column_index)
        if check_row==False or check_other_rows==False or check_box==False:
            return False
        else:
            return True

    @decorate_time
    def solve_grid():
        def recursive_function(grid= test_grid_layout):
            for row_index, row in enumerate(grid):
                for column_index, column in enumerate(row):
                    if  grid[row_index][column_index] == 0:
                        for i in range(1,10):
                            if check_if_valid(i, row_index, column_index):
                                grid[row_index][column_index] = i
                                result = recursive_function()
                                if result is not None:
                                    return result
                                else: 
                                    grid[row_index][column_index] = 0 
                        return 
            print("-------SOLVED SUDOKU GRID--------")
            print(f"{grid[0][0], grid[0][1], grid[0][2]} | {grid[0][3], grid[0][4], grid[0][5]} | {grid[0][6], grid[0][7], grid[0][8]}")
            print(f"{grid[1][0], grid[1][1], grid[1][2]} | {grid[1][3], grid[1][4], grid[1][5]} | {grid[1][6], grid[1][7], grid[1][8]}")
            print(f"{grid[2][0], grid[2][1], grid[2][2]} | {grid[2][3], grid[2][4], grid[2][5]} | {grid[2][6], grid[2][7], grid[2][8]}")
            print("----------+-----------+-----------")
            print(f"{grid[3][0], grid[3][1], grid[3][2]} | {grid[3][3], grid[3][4], grid[3][5]} | {grid[3][6], grid[3][7], grid[3][8]}")
            print(f"{grid[4][0], grid[4][1], grid[4][2]} | {grid[4][3], grid[4][4], grid[4][5]} | {grid[4][6], grid[4][7], grid[4][8]}")
            print(f"{grid[5][0], grid[5][1], grid[5][2]} | {grid[5][3], grid[5][4], grid[5][5]} | {grid[5][6], grid[5][7], grid[5][8]}")
            print("----------+-----------+-----------")
            print(f"{grid[6][0], grid[6][1], grid[6][2]} | {grid[6][3], grid[6][4], grid[6][5]} | {grid[6][6], grid[6][7], grid[6][8]}")
            print(f"{grid[7][0], grid[7][1], grid[7][2]} | {grid[7][3], grid[7][4], grid[7][5]} | {grid[7][6], grid[7][7], grid[7][8]}")
            print(f"{grid[8][0], grid[8][1], grid[8][2]} | {grid[8][3], grid[8][4], grid[8][5]} | {grid[8][6], grid[8][7], grid[8][8]}")
            print("----------------------------------")
        recursive_function()    


    display_unsolved_grid()
    print("\n"*2)
    solve_grid()

sudoku_solver()
    
