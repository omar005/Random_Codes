t = int(input())  # Read the number of test cases

for _ in range(t):
    n,c = input().split() 
    a = [char for char in input()] 
    if c == 'g':
        print(0)
        continue
    dick = {}
    max_dist = 0
    first_occurance_flag = 0
    for i in range(int(n)):
        if  first_occurance_flag == 0:
            if a[i] == c:
                first_occurance_flag = 1
        else:
            if a[i] == 'g': 
                if max_dist < first_occurance_flag:
                    max_dist = first_occurance_flag
                first_occurance_flag = 0
            else:
                first_occurance_flag +=1
    if first_occurance_flag > 0:
        for i in range(int(n)):
            if a[i] == 'g':
                if max_dist < first_occurance_flag:
                    max_dist = first_occurance_flag
                break
            else:
                    first_occurance_flag +=1
    print(max_dist)
