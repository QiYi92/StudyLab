package com.study.Class_And_Object7;

//传参
public class PassArguments
{
    String name; //姓名

    float hp; //血量

    float armor; //护甲

    int moveSpeed; //移动速度

    public PassArguments(){} //构造方法

    //回血
    public void huixue(int xp)
    {
        hp = hp + xp;
        //回血完毕后，血瓶归零
        xp = 0;
    }

    public PassArguments(String name,float hp)
    {
        this.name = name;
        this.hp = hp;
    }

    public static void main(String[] args)
    {
        PassArguments teemo = new PassArguments("提莫",400);
        //小血瓶，回血量100
        int xueping1 = 100;

        //大血瓶，回血量200
        int xueping2 = 200;

        teemo.huixue(xueping1);
        System.out.println(xueping1);
    }
}
