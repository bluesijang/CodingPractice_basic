
#s = input()
# s = "K1KA5CB7"
s = "AJKDLSI412K4JSJ9D"

sum = 0
_str = []
for c in s:
    if ord('A') <= ord(c) <= ord('Z'):
        _str.append(c)
    elif ord('0') <= ord(c) <= ord('9'):
        sum += int(c)

_str.sort()
result = "".join(_str)
print(result+str(sum))
