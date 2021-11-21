digits = input()
digits_list = [int(x) for x in digits]
sums_list = [digits_list[0]]
for i in range(1, len(digits_list)):
    sums_list.append(digits_list[i] + sums_list[i - 1])
print(sums_list)
