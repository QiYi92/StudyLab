package com.study.Train10;

// Animal类，所有动物的抽象父类
public abstract class Animal
{
    // legs属性受保护
    protected int legs; //动物腿的数目
    // 定义一个受保护的构造器，用来初始化legs属性。
    protected Animal(int legs)
    {
        this.legs = legs;
    }

    // 声明抽象方法eat
    public abstract void eat();

    // 声明具体方法walk来打印动物是如何行走的（包括腿的数目）
    public void walk()
    {
        System.out.println("用"+legs+"条腿走路");
    }

}
