# class myclass:
#     """一个简单的类实例"""
#     i = 123
#     def f(self):
#         return 'hello world'
#
# # 实例化类
# x = myclass()
#
# # 访问类的属性和方法
# print("MyClass类的属性i为:",x.i)
# print("MyClass类的方法f输出:",x.f())

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s: %s" % (self.name, self.score))
#
# student = Student('刚子', 90)
# print(student.print_score())


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
