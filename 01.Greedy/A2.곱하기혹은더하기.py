# 1< = len(s) <= 20

# s = input()

s = "02984"

fomula = ""

for n in range(len(s)):
    if n < len(s)-1:
        if s[n] == "0" or s[n] == "1":
            fomula += s[n] + "+"
        else:
            fomula += s[n] + "*"
    else:
        fomula += s[n]

print(f"{fomula} = {eval(fomula)}")
