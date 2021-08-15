package com.study.start1;

public class Item
{
    String name;
    int price;

    public static void main(String[] args)
    {
        Item blood_bottle = new Item();
        blood_bottle.name = "血瓶";
        blood_bottle.price = 50;

        Item grass_shoe = new Item();
        grass_shoe.name = "草鞋";
        grass_shoe.price = 300;

        Item long_sword = new Item();
        long_sword.name = "长剑";
        long_sword.price = 350;

    }
}
