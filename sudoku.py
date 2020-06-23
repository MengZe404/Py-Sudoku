number_grid = [
    ['7', '0', '0', '0', '0', '4', '0', '0', '1', ''], 
    ['0', '2', '0', '0', '6', '0', '0', '8', '0', ''], 
    ['0', '0', '1', '5', '0', '0', '2', '0', '0', ''], 
    ['8', '0', '0', '0', '9', '0', '7', '0', '0', ''], 
    ['0', '5', '0', '3', '0', '7', '0', '2', '0', ''], 
    ['0', '0', '6', '0', '5', '0', '0', '0', '8', ''], 
    ['0', '0', '8', '0', '0', '9', '1', '0', '0', ''], 
    ['0', '9', '0', '0', '1', '0', '0', '6', '0', ''], 
    ['5', '0', '0', '8', '0', '0', '0', '0', '3', '']]


answer_grid = number_grid

size = 9

number_row = [0,0,0,0,0,0,0,0,0]
number_col = [0,0,0,0,0,0,0,0,0]
number_squ = [0,0,0,0,0,0,0,0,0]

possible_array = [1,2,3,4,5,6,7,8,9]

row = 0
col = 0

def generate(row, col):
    # box_position = (row, col)

    global number_row
    global number_col
    global number_squ
    global possible_array

    # All possible values of sukodu
    possible_array = [1,2,3,4,5,6,7,8,9]

    # The square where the object is located
    square_position = (row // 3, col // 3)
    suqare_index = 0

    # The numbers appeard in the same row as the object
    number_row = answer_grid[row]

    # Get all the appeared numbers on the same coloum as the object
    for row in range(0, 9):
        number_col[row] = answer_grid[row][col]

    for x in range(square_position[0] * 3, square_position[0] * 3 + 3):
        for y in range(square_position[1] * 3, square_position[1] * 3 + 3):
            number_squ[suqare_index] = answer_grid[x][y]
            suqare_index += 1

    # Illiterate the number_row and remove the appeared number from possible_array
    for i in number_row:
        if i == '':
            pass
        elif int(i) in possible_array:
            possible_array.remove(int(i))

    # Illiterate the number_col and remove the appeared number from possible_array
    for j in number_col:
        if j == '':
            pass
        elif int(j) in possible_array:
            possible_array.remove(int(j))

    for n in number_squ:
        if n == '':
            pass
        elif int(n) in possible_array:
            possible_array.remove(int(n))
    
    return possible_array

correct = False

def check(row):
    global correct

    sum = 0

    for i in range(len(answer_grid[row])):
        if answer_grid[row][i] != '':
            sum += int(answer_grid[row][i])

    if sum == 45:
        correct = True
    else:
        correct = False

answer_index = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

# Run the function for every object
def run():
    global answer_index
    global answer_grid

    row = 0
    col = 0
    for row in range(0, size):
        for col in range(0, size):
                generate(row, col)

                if answer_grid[row][col] == '0':
                    if len(possible_array):
                        answer_grid[row][col] = str(possible_array[answer_index[row][col]])
                    # else:
                    #     if int(answer_grid[row][col]) < len(possible_array):
                    #         answer_grid[row][col] += 1
                    #         run()
        check(row)
        if correct == True:
            pass
        else:
            if int(answer_grid[row][col]) < len(possible_array):
                answer_grid[row][col] += 1
            # run()


run()
print(answer_grid)


# 7 8 5 9 2 4 6 3 1
# 9 2 4 1 6 3 5 8 7
# 6 3 1 5 7 8 2 4 9
# 8 4 3 6 9 2 7 1 5
# 1 5 9 3 8 7 4 2 6
# 2 7 6 4 5 1 3 9 8
# 4 6 8 7 3 9 1 5 2
# 3 9 7 2 1 5 8 6 4
# 5 1 2 8 4 6 9 7 3