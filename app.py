import itertools

# naive divisors generation approach
def get_divisors(n):
    for i in range(1, n+1):
        if n % i == 0 and i != n: # don't include the number itself for this
            yield i

# 100 room numbers max
for i in range(1, 100):
    d = list(get_divisors(i))
    if sum(d) > i:
        found_sum = False
        for a in range(1, len(d)): # generate permutations of each subset
            for p in itertools.permutations(d, a):
                if sum(p) == i:
                    found_sum = True
                    break
            if found_sum:
                break
        if not found_sum:
            print(i)
