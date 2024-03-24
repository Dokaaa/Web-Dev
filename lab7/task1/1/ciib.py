N = int(input())
for divisor in range(2, N + 1):
    if N % divisor == 0:
        print(divisor)
        break