package com.study.Class_And_Object7;

public class Support extends Hero
{
    public void heal()
    {
        System.out.println(name + "进行了一次治疗，但是并没有目标");
    }
    public void heal(Hero h)
    {
        System.out.println(name + "对"+h.name+"进行了一次治疗");
    }
    public void heal(Hero h, int hp)
    {
        System.out.println(name + "对"+h.name+"进行了一次治疗,回复了"+hp+"点HP");
    }


    public static void main(String[] args)
    {
        Support sh = new Support();
        sh.name = "奶妈";

        Hero h = new Hero();
        h.name = "盖伦";

        sh.heal(h);
        sh.heal(h,100);

    }
}
