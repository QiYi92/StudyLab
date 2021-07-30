package com.study.Inner_Classes;

import com.study.Polymorphic_Train.Hero;

public abstract class Hero2
{
    //本地类样本
    String name; //姓名
    float hp; //血量
    float armor; //护甲
    int moveSpeed; //移动速度

    public abstract void attack();
    public static void main(String[] args)
    {
        //与匿名类的区别在于，本地类有了自定义的类名
        class SomeHero extends Hero2
        {
            public void attack()
            {
                System.out.println(name + "新的进攻手段");
            }
        }
        SomeHero h = new SomeHero();
        h.name = "地卜师";
        h.attack();
    }
}
