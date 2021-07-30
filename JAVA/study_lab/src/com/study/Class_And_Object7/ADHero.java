package com.study.Class_And_Object7;
//attack方法重载
//为ADHero 提供三种方法
//
//public void attack()
//public void attack(Hero h1)
//public void attack(Hero h1, Hero h2)
import restart.Hero;
public class ADHero extends Hero
{
    public void attack()
    {
        System.out.println(name + "进行了一次攻击，但是不确定打中谁");
    }
    public void attack(Hero h1)
    {
        System.out.println(name+"对"+ h1.name + "进行了一次攻击 ");
    }
    public void attack(Hero h1, Hero h2) {
        System.out.println(name + "同时对" + h1.name + "和" + h2.name + "进行了攻击 ");
    }
    public void attack(Hero... heroes)
    {
        for(int i = 0; i < heroes.length;i++)
        {
            System.out.println(name+"攻击了"+heroes[i].name);
        }
    }

    public static void main(String[] args)
    {
        ADHero bh = new ADHero(); //AD英雄类新创建一个对象
        bh.name = "赏金猎人";

        Hero h1 = new Hero();
        h1.name = "盖伦";

        Hero h2 = new Hero();
        h2.name = "提莫";

        bh.attack(h1);
        bh.attack(h1,h2);
    }

}
