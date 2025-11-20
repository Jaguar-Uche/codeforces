import math
import string
chars = string.ascii_uppercase

def return_col_number(alpha):
    col_number = 0
    while len(alpha) >= 1:
        col_number += (math.pow(26, len(alpha) - 1)) * (chars.index(alpha[0]) + 1)
        alpha = alpha[1:]
    return int(col_number)

def get_RxCy_form(cell_name):
    str_part =""
    i = 0
    while i < len(cell_name) and cell_name[i].isalpha():
        str_part += cell_name[i]
        i += 1
    number_part = cell_name[i:]

    if len(str_part) == 1:
        return "R" + number_part + "C" + str(chars.index(str_part)+1)
    else:
        return "R" + number_part + "C" + str(return_col_number(str_part))


def get_AnoBno_form(Rxcy):
    Rxcy = Rxcy[1:]
    list = Rxcy.split("C")
    row_string = list[0]
    col_string = list[1]

    col_number = int(col_string)
    col_string = ""
    col_list = []
    while col_number > 0:
        col_number -= 1
        col_list.append(col_number % 26)
        col_number //= 26

    for col in reversed(col_list):
        col_string += chars[col]

    return f"{col_string}" + f"{row_string}"

n = int(input())

cell = []
for _ in range(n):
    cell.append(input().strip())

for num_sys in cell:
    if num_sys[0] == "R" and num_sys[1].isdigit() and 'C' in num_sys:
        other_form = get_AnoBno_form(num_sys)
    else:
        other_form = get_RxCy_form(num_sys)
    print(other_form)