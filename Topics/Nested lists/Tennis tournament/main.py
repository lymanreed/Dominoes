lines = int(input())
winners = []
wins = 0
for _ in range(lines):
    data = input().split()
    if data[1] == "win":
        winners.append(data[0])
        wins = wins + 1
print(winners)
print(wins)
