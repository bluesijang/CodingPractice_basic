# 정수 N 입력 => 00:00:00 ~ N:59:59 까지 숫자 3이 하나 이상인 시각을 모두 구하시요
# 0 <= N <=23

n = int(input())
result = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if ('3' in str(s)) or ('3' in str(m)) or ('3' in str(h)):
                result += 1

print(result)
