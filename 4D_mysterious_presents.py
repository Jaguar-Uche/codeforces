n, w, h = map(int, input().split())

envelopes = []
for i in range(n):
    wi, hi = map(int, input().split())
    if wi > w and hi > h:  # must fit card
        envelopes.append((wi, hi, i + 1))  # store original index

# If no envelope fits
if not envelopes:
    print(0)

# Sort by width, then height
envelopes.sort()

m = len(envelopes)
dp = [1] * m
parent = [-1] * m

max_len = 1
max_idx = 0

# LIS in 2D
for i in range(m):
    for j in range(i):
        if (envelopes[j][0] < envelopes[i][0] and
                envelopes[j][1] < envelopes[i][1] and
                dp[j] + 1 > dp[i]):
            dp[i] = dp[j] + 1
            parent[i] = j

    if dp[i] > max_len:
        max_len = dp[i]
        max_idx = i

# Reconstruct chain
chain = []
cur = max_idx
while cur != -1:
    chain.append(envelopes[cur][2])  # original index
    cur = parent[cur]

chain.reverse()

print(max_len)
print(*chain)
