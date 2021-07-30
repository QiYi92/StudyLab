package com.study.Polymorphic_Train;

public class Armor extends Item
{
    int ac; //护甲等级

    @Override
    public boolean disposable()
    {
        return false;
    }
}
