a = [1, 2, 3, 3, 4, 4]
s = {}
repeated = None

for i in a:
    if i in s:
        repeated = i
        break
    else:
        s[i] = 1

if repeated:
    print("Repeated integer:", repeated)
else:
    print("No repeated integers found.")
