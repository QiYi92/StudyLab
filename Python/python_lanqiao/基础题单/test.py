def GCD(num1,num2):
    # 两正整数相除，取被除数和余数成为新的两个数，再相除
    # 当余数为0时，被除数就是最大公因数
    if num2 > num1:
        num1,num2=num2,num1
    while num1 % num2 != 0:
        num1,num2 = num2,num1 % num2
    return num2

print(GCD(200,100))