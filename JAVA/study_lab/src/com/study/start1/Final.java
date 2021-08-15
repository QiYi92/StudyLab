package com.study.start1;

public class Final
{
    //final 修饰一个变量，有很多种说法，比如不能改变等等
    //准确的描述是 当一个变量被final修饰的时候，该变量只有一次赋值的机会

    public void method1()
    {
        final int i =5;
        //i = 10; //i在第4行被final赋值了,所以报错
    }
    public void method2()
    {
        final int i;
        //i在第15行，只是被声明，但是没有被赋值，所以在这里可以进行第一次赋值
        i=10;
        //i在第6行已经被赋值过了，所以这里会出现编译错误
        //i=11;
    }
    public void method3(final int j)
    {
        //j = 5; //是否可执行？
        //不可以，因为在调用方法的时候，就一定会第一次赋值了，后面不能再进行多次赋值
    }
}
