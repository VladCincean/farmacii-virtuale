import random
import string
import statistics

# 2. Lottery

# Ball = tuple ('w'/'b', letter)

# L1 'white'/'blue'
# L2 litere

# 1.
def generate(n, p, k):
    L1 = ['white'] * p + ['blue'] * (n - p)
    random.shuffle(L1)
    L2 = [random.choice(string.ascii_uppercase) for _ in range(n)]
    
    return L1[:k], L2[:k]

# 2.
def check(L1, L2, a):
    return (set(L2) & set(['A', 'E', 'I', 'O', 'U'])) != set() \
            and L1.count('white') >= a

# 3.
def fitness(L1, L2, a):
    f = max(0, L1.count('blue') - (len(L1) - a))
    if set(L2) & set(['A', 'E', 'I', 'O', 'U']) == set():
        f += 1
    
    return f

# 4.
def mean_and_stdev(N, n, p, k, a):
    pop = [generate(n, p, k) for _ in range(N)]
    f = [fitness(pop[i][0], pop[i][1], a) for i in range(N)]

    mean = statistics.mean(f)
    stdev = statistics.stdev(f)

    return mean, stdev


# main
m, s = mean_and_stdev(N = 60, n = 40, p = 10, k = 30, a = 10)

print("mean = " + str(m))
print("stdev = " + str(s))
