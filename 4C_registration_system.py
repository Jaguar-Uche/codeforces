dict = {}
output = []

n = input().strip()
for _ in range(int(n)):
    name = input().strip()
    if name in dict.keys():
        original_name = name
        name += str(dict[name])
        dict[original_name] += 1
        dict[name] = 1
        output.append(name)
    else:
        dict[name] = 1
        output.append("OK")

for result in output:
    print(result)