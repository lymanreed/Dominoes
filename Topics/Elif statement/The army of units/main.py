units = int(input())

print(
    "no army" if units < 1 else
    "few" if units < 10 else
    "pack" if units < 50 else
    "horde" if units < 500 else
    "swarm" if units < 1000 else
    "legion"
)
