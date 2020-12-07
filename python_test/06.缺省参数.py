def pow(x, n=2):
    ret = 1
    while n > 0:
        ret *= x
        n -= 1
    return ret


print(pow(5)) # 变化小的作为默认参数
