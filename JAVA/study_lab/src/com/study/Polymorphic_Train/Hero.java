package com.study.Polymorphic_Train;

public class Hero
{
    public String name;
    protected float hp;

    public void kill(Mortal m)
    {
        System.out.println(name + "放了一个大招");
        m.die();
    }

    //类方法，静态方法
    //通过类就可以直接调用
    public static void battleWin()
    {
        System.out.println("hero battle win");
    }

    public static void main(String[] args)
    {


        Hero h = new Hero();
        h.name = "盖伦";

        ADHero ad = new ADHero();
        ad.name = "艾希";

        APHero ap = new APHero();
        ap.name = "安妮";

        ADAPHero adap = new ADAPHero();
        adap.name = "库奇";



        h.kill(ad);
        h.kill(ap);
        h.kill(adap);
    }
}
