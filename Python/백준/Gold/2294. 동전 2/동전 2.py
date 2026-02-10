n, k = [*map(int, input().split())]

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [1e8 for _ in range(k + 1)]
dp[0] = 0

for coin in coins:
    for value in range(coin, k+1):
        dp[value] = min(dp[value], dp[value-coin] + 1)
        
answer = dp[k] if dp[k] != 1e8 else -1
print(answer)