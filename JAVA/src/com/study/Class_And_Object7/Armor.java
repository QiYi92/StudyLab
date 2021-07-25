package com.study.Class_And_Object7;

public class Armor extends Item
{
    int ac; //护甲等级

    public static void main(String[] args)
    {
        Armor LeatherArmor = new Armor();
        LeatherArmor.ac = 30;

        LeatherArmor.name = "皮革护甲";
        LeatherArmor.price = 5000;

        Armor ChainArmor = new Armor();
        ChainArmor.ac = 50;

        ChainArmor.name = "锁链护甲";
        ChainArmor.price = 7000;

    }

}
