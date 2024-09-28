t = int(input())  # Read the number of test cases

for _ in range(t):
    n = int(input())  # Length of the array and string
    a = list(map(int, input().split()))  # Read the array a
    s = input()  # Read the string s
    for i in range(len(a)):
        for j in range(i+1, len(s)):
            if a[i] == a[j]:
                if not s[i] == s[j]:
                    print('NO')
                    break  # Exit the inner loop
        else:
            continue  # Continue if inner loop was not broken
        break  # Break the outer loop if inner loop was broken
    else:
        print('YES')

