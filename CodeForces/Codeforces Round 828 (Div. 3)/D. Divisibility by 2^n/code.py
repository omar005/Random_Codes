import math
from heapq import heappush, heappop

class Divisible:
    def __init__(self):
        self.max_n = 10**6
        self.twos_count = [self.count_twos_in_prime_factors(i) for i in range(self.max_n + 1)]
    
    def count_twos_in_prime_factors(self, num):
        if num <= 0:
            return 0
        return (num & -num).bit_length() - 1
    
    def solve(self, arr, n):
        count_twos_in_arr = sum(self.twos_count[num] if num <= self.max_n else self.count_twos_in_prime_factors(num) for num in arr)
        if count_twos_in_arr >= n:
            return 0
        
        heap = []
        for i in range(1, n+1):
            heappush(heap, -self.twos_count[i])
        
        extra_twos_needed = n - count_twos_in_arr
        count = 0
        while extra_twos_needed > 0 and heap:
            extra_twos_needed += heappop(heap)
            count += 1
        
        return count if extra_twos_needed <= 0 else -1

t = int(input())
d_class = Divisible()
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(d_class.solve(a, n))