# n = input()
# n = "123402"
n = "7799"
input_data = "123402"

a = list(n[:len(n)//2])
b = list(n[len(n)//2:])

s1 = sum([int(i) for i in a])
s2 = sum([int(i) for i in b])

if s1 == s2:
    print("LUCKY")
else:
    print("READY")
