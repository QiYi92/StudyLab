"""
1：两个字符串长度不等。比如 Beijing 和 Hebei
2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing
3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和 BEIjing
4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing
"""

class Solution:
    def __strcmp__(self,str1,str2): #字符串比较函数
        if str1.upper()==str2.upper():
            if str1==str2:
                return (2) #完全一致
            else:
                return (3) #不区分大小写一致
        elif len(list(str1))!=len(list(str2)):
            return (1) #长度不等
        else:
            return (4) #长度相等

str1=input()
str2=input()
s=Solution()
print(s.__strcmp__(str1,str2))