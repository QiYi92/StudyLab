package com.study.Inner_Classes;

import com.study.Interface10.AD;
import com.study.Interface10.Hero;

public class ADHero extends Hero implements AD
{
    @Override
    public void physicAttack()
    {
        System.out.println("进行物理攻击");
    }

    public void attack() {
    }
}
