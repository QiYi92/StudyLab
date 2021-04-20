s = str(input())
n,zimu = 0,''
for i in range(len(s)):
    if s.count(s[i]) > n:
        n = s.count(s[i])
        zimu = s[i]
print(zimu)
print(n)