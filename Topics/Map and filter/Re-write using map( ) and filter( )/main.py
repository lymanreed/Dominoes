even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

my_sum = list(map(lambda e, o: e + o, even, odd))

remainders = list(map(lambda n: n % 3, my_sum))

nonzero_remainders = list(filter(lambda r: r, remainders))
