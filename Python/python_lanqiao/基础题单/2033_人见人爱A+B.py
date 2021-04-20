# 人见人爱A+B
n = int(input())
for i in range(n):
    AH, AM, AS, BH, BM, BS = map(int, input().split())
    CH,CM,CS=AH+BH,AM+BM,AS+BS
    if CM >= 60:
        CH += 1
        CM = CM-60
    if CS >= 60:
        CM += 1
        CS = CS-60
    print(CH,CM,CS)

