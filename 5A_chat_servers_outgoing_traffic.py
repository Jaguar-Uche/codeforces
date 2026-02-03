
users_list = []
traffic = 0

while True:
    try:
        line = input()
        if not line:
            break
        if line[0] == "+":
            users_list.append(line[1::])
        elif line[0] == "-":
            users_list.remove(line[1::])
        else:
            message_list = line.split(":")
            traffic += len(users_list) * len(message_list[1])
    except EOFError:
        break
print(traffic)