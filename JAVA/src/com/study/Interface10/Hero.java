package com.study.Interface10;

public class Hero
{
    public String name; //姓名

    protected float hp; //血量

    static String copyright; //类属性，静态属性


    float armor; //护甲

    int moveSpeed; //移动速度

    public void showAddressInMemory()
    {
        System.out.println("打印this看到的虚拟地址："+this);
    }

    //实例方法，对象方法，非静态方法
    //必须有对象才能够调用
    public void die()
    {
        hp = 0;
    }

    //类方法，静态方法
    //通过类就可以直接调用
    public static void battleWin()
    {
        System.out.println("battle win");
    }

    public static void main(String[] args)
    {
        Hero garen = new Hero();
        garen.name = "盖伦";
        //类属性 不同对象共享一个类属性
        Hero.copyright = "版权由Riot Games公司所有";

        System.out.println(garen.copyright);
    }


}

