n = int(input())

k = n

sum = 0

while(n):
    a = n % 10
    sum += (a**3)
    n = n // 10

if sum == k:
    print("YES")
else:
    print("NOOOOOOOOO")

