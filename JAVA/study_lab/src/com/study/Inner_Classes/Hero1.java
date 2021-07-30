package com.study.Inner_Classes;

public abstract class Hero1
{
    String name; //姓名

    float hp; //血量

    float armor; //护甲

    int moveSpeed; //移动速度

    public abstract void attack();

    public static void main(String[] args)
    {

        ADHero adh=new ADHero();
        //通过打印adh，可以看到adh这个对象属于ADHero类
        adh.attack();
        System.out.println(adh);

        Hero1 h = new Hero1()
        {
            //当场实现attack方法
            public void attack()
            {
                System.out.println("新的进攻手段");
            }
        };
        h.attack();
        //通过打印h，可以看到h这个对象属于Hero$1这么一个系统自动分配的类名

        System.out.println(h);
    }
}
