def get_shortest_path(s,t):
    letters = ("a", "b", "c", "d", "e", "f", "g", "h")
    current_rank = int(s[1])
    target_rank = int(t[1])
    current_file = letters.index(s[0])
    target_file = letters.index(t[0])
    moves = []
    while current_rank != target_rank or current_file != target_file:
        if current_file > target_file and current_rank < target_rank:
            current_rank += 1
            current_file -=1
            moves.append("LU")
        elif current_file > target_file and current_rank > target_rank:
            current_file -= 1
            current_rank -= 1
            moves.append("LD")
        elif current_file < target_file and current_rank < target_rank:
            current_file += 1
            current_rank += 1
            moves.append("RU")
        elif current_file < target_file and current_rank > target_rank:
            current_file += 1
            current_rank -= 1
            moves.append("RD")
        elif current_file < target_file:
            current_file += 1
            moves.append("R")
        elif current_file > target_file:
            current_file -= 1
            moves.append("L")
        elif current_rank > target_rank:
            current_rank -= 1
            moves.append("D")
        elif current_rank < target_rank:
            current_rank += 1
            moves.append("U")

    print(len(moves))
    for move in moves:
        print(move)

current_position= input().strip()
target_position = input().strip()
get_shortest_path(current_position, target_position)