# 2026统计元音
n = int(input())
for i in range(n):
    s = str(input())
    a_num = s.count('a')
    e_num = s.count('e')
    i_num = s.count('i')
    o_num = s.count('o')
    u_num = s.count('u')
    print(f"a:{o_num}")
    print(f"e:{o_num}")
    print(f"i:{o_num}")
    print(f"o:{o_num}")
    print(f"u:{u_num}")
    if i!=n:
        print('')