def find_possibility(big_list):
    list1 = big_list[0]
    list2 = big_list[1]
    list3 = big_list[2]
    count_X = 0
    count_O = 0
    count_period = 0
    X_won = False
    O_won = False
    checker =0
    for letter in list1:
        if letter == 'X':
            count_X += 1
        elif letter == 'O':
            count_O += 1
        elif letter == '.':
            count_period += 1
    for letter in list2:
        if letter == 'X':
            count_X += 1
        elif letter == '.':
            count_period += 1
        elif letter == 'O':
            count_O += 1
    for letter in list3:
        if letter == 'X':
            count_X += 1
        elif letter == '.':
            count_period += 1
        elif letter == 'O':
            count_O += 1
    while checker < 1:
        if 'X' == list1[0]:
            if list1[0] == list1[1] == list1[2]:
                X_won = True
                break
            elif list1[0] == list2[0] == list3[0]:
                X_won = True
                break
            elif list1[0] == list2[1] == list3[2]:
                X_won = True
                break
        elif 'O' == list1[0]:
            if list1[0] == list1[1] == list1[2]:
                O_won = True
                break
            elif list1[0] == list2[0] == list3[0]:
                O_won = True
                break
            elif list1[0] == list2[1] == list3[2]:
                O_won = True
                break
        elif 'O' == list1[0]:
            if list1[0] == list1[1] == list1[2]:
                O_won = True
                break
            elif list1[0] == list2[0] == list3[0]:
                O_won = True
                break
            elif list1[0] == list2[1] == list3[2]:
                O_won = True
                break

        if 'X' == list1[2]:
            if list1[2] == list2[1] == list3[0]:
                X_won = True
                break
            elif list1[2] == list2[2] == list3[2]:
                X_won = True
                break
        elif 'O' == list1[2]:
            if list1[2] == list2[1] == list3[0]:
                O_won = True
                break
            elif list1[2] == list2[2] == list3[2]:
                O_won = True
                break

        if 'X' == list1[1]:
            if list1[1] == list2[1] == list3[1]:
                X_won = True
        elif 'O' == list1[1]:
            if list1[1] == list2[1] == list3[1]:
                O_won = True

        if 'X' == list2[0]:
            if list2[0] == list2[1] == list2[2]:
                X_won = True
                break
        elif 'O' == list2[0]:
            if list2[0] == list2[1] == list2[2]:
                O_won = True
                break

        if 'X' == list3[0]:
            if list3[0] == list3[1] == list3[2]:
                X_won = True
                break
        elif 'O' == list3[0]:
            if list3[0] == list3[1] == list3[2]:
                O_won = True
                break
        checker+=1
    if count_X >= count_O:
        if O_won and X_won:
            print('illegal')
        elif O_won and count_X > count_O:
            print('illegal')
        elif X_won and count_X == count_O or count_X-count_O > 1:
            print('illegal')
        elif X_won:
            print("the first player won")
        elif O_won:
            print("the second player won")
        elif count_X - count_O > 1:
            print('illegal')
        elif count_O == count_X:
            print("first")
        elif count_X != 5 and count_X > count_O:
            print("second")
        elif count_X == 5 and count_O == 4 and count_period == 0:
            print("draw")
    else:
        print("illegal")

biggest_list =[]
for _ in range(3):
    line = input()
    x= line[0]
    y= line[1]
    z= line[2]
    if x.isdigit():
        x = 'O'
    if y.isdigit():
        y = 'O'
    if z.isdigit():
        z = 'O'
    first_list = [x,y,z]
    biggest_list.append(first_list)
print(biggest_list)
find_possibility(biggest_list)