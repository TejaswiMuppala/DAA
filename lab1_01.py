import time
import matplotlib.pyplot as plt

def iterative_sum(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum

def recursive_sum(N):
    if N == 0:
        return 0
    else:
        return N + recursive_sum(N-1)

def measure_time(func, N):
    start_time = time.time()
    func(N)
    return (time.time() - start_time) * 1000  # Convert seconds to milliseconds

Ns = list(range(1, 1001, 50))
iterative_times = []
recursive_times = []

for N in Ns:
    iterative_time = measure_time(iterative_sum, N)
    recursive_time = measure_time(recursive_sum, N)
    iterative_times.append(iterative_time)
    recursive_times.append(recursive_time)

plt.plot(Ns, iterative_times, label='Iterative')
plt.plot(Ns, recursive_times, label='Recursive')
plt.xlabel('N')
plt.ylabel('Time (milliseconds)')
plt.title('Time taken to compute sum of first N natural numbers')
plt.legend()
plt.show()
