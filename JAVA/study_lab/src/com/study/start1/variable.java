package com.study.start1;

public class variable
{
    //当一个变量被声明在类下面
    //变量就叫做字段 或者属性、成员变量、Field
    //比如变量i,就是一个属性。
    //那么从第2行这个变量声明的位置开始，整个类都可以访问得到
    //所以其作用域就是从其声明的位置开始的整个类

    int i = 1;
    int j = i; //其他属性可以访问i
    public void method1()
    {
        System.out.println(i);
        //方法1可以访问i
    }
    public void method2()
    {
        System.out.println(i);
        //方法2也可以访问i
    }

    //如果一个变量，是声明在一个方法上的，就叫做参数
    //参数的作用域即为该方法内的所有代码
    //其他方法不能访问该参数
    //类里面也不能访问该参数

    public void method3(int j)
    {
        System.out.println(j);
        //参数i的作用域即方法method3
    }
    public  void method4()
    {
        System.out.println(j);
        //method4不能访问参数i
    }
    int a = j; //类里面也不能访问参数i

    //声明在方法内的变量，叫做局部变量
    //其作用域在声明开始的位置，到其所处于的块结束位置
    public void method5()
    {
        int i = 5;
        //其作用范围是从声明的第45行
        //到其所于的块结束的第57行
        System.out.println(i);
        {
            //子块
            System.out.println(i);//可以访问i
            int j = 6;
            System.out.println(j);//可以访问j
        }
        System.out.println(j);
        //不能访问j，因为其作用域到第54行就结束了
    }
    //练习作用域
    //属性的作用域在方法中，参数的作用域也在方法中
    //如果属性和参数命名相同了的话？ 那么到底取哪个值？
    int k = 1; //属性名是k
    public void method6(int k)
    {
        //参数也是k
        System.out.println(k);
    }
    public static void main(String[] args)
    {
        new variable().method6(5);
        //结果打印出来是1还是5？

        //answer:5
        //输出是5，当访问的变量被多个作用域影响的时候，按照就近原则取

    }

}

