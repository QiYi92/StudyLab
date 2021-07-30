package com.study.Polymorphic_Train;

import com.study.Interface10.AD;

public class ADHero extends Hero implements AD,Mortal
{
    @Override
    public void physicAttack()
    {

    }

    @Override
    public void die() {
        System.out.println(name+ " 这个物理英雄挂了");
    }

    //隐藏父类的battleWin方法
    public static void battleWin()
    {
        System.out.println("ad hero battle win");
    }
    public static void main(String[] args)
    {
        Hero.battleWin();
        ADHero.battleWin();
    }
}

