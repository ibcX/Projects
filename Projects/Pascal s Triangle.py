
def print_function(row_list):
    row_str = ""
    for index in row_list:
        if index == 0:
            row_str = row_str + " "
        else:
            row_str = row_str + str(index)
    print(row_str)


def row_calculation(row_num):
    row_num_plus_1 = []
    index = 0
    while index <= rows * 2:
        if index == 0:
            row_num_plus_1.append(0)
        elif index == rows * 2:
            row_num_plus_1.append(0)
        else:
            num = row_num[index - 1] + row_num[index + 1]
            row_num_plus_1.append(num)
        index += 1
    print_function(row_num_plus_1)
    return row_num_plus_1


def row_1_calc():
    row_1 = rows * " " + "1" + rows * " "
    row_1_int = []
    for letter in row_1:
        if letter == " ":
            row_1_int.append(0)
        elif letter == "1":
            row_1_int.append(1)
    print_function(row_1)
    return row_1_int


rows = int(input("""
    Printing Pascal’s triangle
Please insert the number of rows: """))

if rows >= 1:
    row_1_int = row_1_calc()
    for row in range(1, rows):
        if row == 1:
            new_row = row_calculation(row_1_int)
        else:
            new_row = row_calculation(new_row)
