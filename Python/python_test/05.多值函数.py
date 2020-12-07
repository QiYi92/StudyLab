"""
一个函数中，，如果要处理的函数的参数类型不确定
参数名前加   *可以接收 元组类型—————— *args
参数名前加  **可以接收 字典类型—————— *kwargs
"""


# def demo(num, *args, **kwargs):
#     print(num) # 获取第一个数字
#     print(args) # 获取元组序列
#     print(kwargs) # 获取字典
#
#
# demo(1, 2, 3, 4, 5, 6, 7, 8, 92, 7, "A",name="祺熠", age=18, gender=True)


# 元组求和
def sum_number(*args):
    ret = 0
    for i in args:
        print(i)
        ret += i
    return ret

ret = sum_number(1, 2, 3, 4, 5)
print(ret)


def demo(*args, **kwargs):
    print(args)
    print(kwargs)

num1 = (1, 2, 3)
s_dict = {'name':"祺熠", 'age':18}

demo(*num1, **s_dict)
