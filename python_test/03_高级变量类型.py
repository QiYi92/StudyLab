# l = [1, 2, 3, 4]
# s = [7, 8, 9]
# print(l)
#
# #增加
# l.insert(0, 5) #在第1列插入5
# print(l)
# l.append(6) #在数列末尾添加6
# print(l)
# l.extend(s) #在数列末尾插入数列s
# print(l)
#
# #删除
# del l[2] #删除数列中的2
# print(l)
# l.remove(8) #删除数列中的8
# print(l)
# l.pop() #删除末尾列的数字
# print(l)
# l.pop(-5) #删除倒数第五列的数字
# print(l)
#
# #修改
# l[1] = 2
# print(l) #删除第1列的数字（从第0列开始）
#
# #排序
# l.sort() #正序排列数组
# print(l)
# l.sort(reverse=True) #倒序排列数组
# print(l)
#
# for i in l:
#     print(i)

info = (2018, "AK47", 2019, 2019,)
print(type(info)) #类型为元组
print(info.count(2019)) #数据中有几个2019
print(info.index("AK47")) #数据中"AK47"在什么位置

s_dict = {"name": "祺熠",
          "age": 20,
          "gender": True,
          "height": 1.80
          }

print(s_dict.keys()) #keys取到序列
print(s_dict.values()) #values取到值
print(s_dict.items()) #两者都取


