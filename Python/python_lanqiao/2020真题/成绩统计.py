n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
jige = 0
youxiu = 0

for j in range(len(s)):
    if s[j] >= 60:
        jige += 1
        if s[j] >= 85:
            youxiu += 1
jige_number = int(round(jige / n,2) * 100)
youxiu_number = int(round(youxiu / n,2) * 100)

print(f"{jige_number}%")
print(f"{youxiu_number}%")