# len(s) < 10^6
s = input()

d = [0] * 2
prev = ""

for i in s:
    if i == '0':
        if i != prev:
            d[0] += 1
    else:
        if i != prev:
            d[1] += 1

    prev = i

print(min(d))
