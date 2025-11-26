def get_winner(rounds):
    # Step 1: compute final scores
    final_scores = {}
    for name, score in rounds:
        final_scores[name] = final_scores.get(name, 0) + score
    #     final_scores.get(name,0) returns the score of the player or 0 if the player hasn't been entered

    max_score = max(final_scores.values())
    # This gets the highest score at the end

    # Step 2: find who reaches max first
    cumulative = {}
    for name, score in rounds:
        cumulative[name] = cumulative.get(name, 0) + score
        if cumulative[name] >= max_score and final_scores[name] == max_score:
            # It returns only the person that reaches the highest score first and still has the same amount of points at the end
            return name


n = int(input())
lists = []

for _ in range(n):
    input_name, input_score = input().split()
    input_score = int(input_score)
    lists.append([input_name, input_score])

winner = get_winner(lists)
print(winner)