package com.study.Polymorphic_Train;

public class ADAPHero extends Hero implements AD,AP,Mortal
{
    @Override
    public void magicAttack() {
        // TODO Auto-generated method stub

    }

    @Override
    public void physicAttack() {
        // TODO Auto-generated method stub

    }

    @Override
    public void die() {
        System.out.println(name+ " 这个混合英雄挂了");
    }
}
