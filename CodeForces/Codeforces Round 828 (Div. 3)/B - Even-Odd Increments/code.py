def count_odd(arr):
    counter = 0
    for i in arr:
        if i%2 == 1:
            counter += 1
    return counter
    
t = int(input())  # Read the number of test cases

for _ in range(t):
    n,q = input().split()
    a = list(map(int, input().split()))  # Read the array a
    ODD = count_odd(a)
    EVEN = len(a) - ODD
    cumu_val = 0
    init_sum = sum(a)
    for _ in range(int(q)): 
       odd, added_val = input().split()
       odd = int(odd)
       added_val = int(added_val)
       
       cumu_val += added_val * ((EVEN*(1- odd))+(ODD*odd))

       if odd == 1 and added_val %2 == 1:
           EVEN = len(a)
           ODD = 0
       elif odd == 0 and added_val %2 == 1:
           EVEN = 0
           ODD = len(a) 
       returned = init_sum + cumu_val     
       print(returned)





#Exceed time limit
"""
t = int(input())  # Read the number of test cases
 
for _ in range(t):
    n,q = input().split()
    a = list(map(int, input().split()))  # Read the array a
    for _ in range(int(q)):
       odd, added_val = input().split() 
       for i in range(len(a)):
           if a[i]%2 == int(odd):
               a[i]+= int(added_val)
       print(sum(a))
""" 