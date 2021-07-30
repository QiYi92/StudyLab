package com.study.Class_And_Object7;

public class This2
{
    String name; //姓名

    float hp; //血量

    float armor; //护甲

    int moveSpeed; //移动速度

    //带一个参数的构造方法
    public This2(String name)
    {
        System.out.println("一个参数的构造方法");
        this.name = name;
    }
    //带两个参数的构造方法
    public This2(String name, float hp)
    {
        this(name); //this()在一个构造方法中调用另一个构造方法
        System.out.println("两个参数的构造方法");
        this.hp = hp;
    }

    public static void main(String[] args)
    {
        This2 teemo = new This2("提莫",400);
        System.out.println(teemo.name+" "+teemo.hp);
    }
}
