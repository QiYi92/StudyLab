package com.study.Inner_Classes;

public abstract class Item
{
    //匿名类练习
    String name;
    int price;

    public abstract boolean disposable();

    public static void main(String[] args)
    {
        Item i = new Item() {
            @Override
            public boolean disposable() {
                return false;
            }
        };
        System.out.println(i.disposable());
    }
}
