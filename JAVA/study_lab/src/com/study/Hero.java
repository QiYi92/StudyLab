package com.study;

public class Hero //所有的英雄都是hero类
{
    //hero类的属性
    String name; //姓名
    float hp; //血量
    float armor; //护甲
    int moveSpeed; //移动速度

    //hero类的方法
    float getArmor() //获取护甲值的方法
    {
        return armor;
    }

    float getmoveSpeed() //获取移动速度的方法
    {
        return moveSpeed;
    }

    float getHp() //获取hp的方法
    {
        return hp;
    }

    void kill() //杀敌方法
    {
        System.out.println("击杀敌方hero");
    }

    void legendary() //超神方法
    {
        System.out.println("完成一次超神");
    }

    float recovery(float blood)
    {
        hp = hp + blood;
        return hp;
    }

    void addSpeed(int speed) //增加移动速度的方法
    {
        //在原来的基础上增加移动速度
        moveSpeed = moveSpeed + speed;
    }


    public static void main(String[] args)
    {
        Hero garen = new Hero(); //对象创建
        garen.name = "garen";
        garen.hp = 123.45f;
        garen.armor = 98.765f;
        garen.moveSpeed = 350;
        garen.addSpeed(100);


        Hero teemo = new Hero();
        teemo.name = "teemo";
        teemo.hp = 345f;
        teemo.armor = 14f;
        teemo.moveSpeed = 200;
        teemo.recovery(200f);

        //调用方法
        garen.kill();
        System.out.println(garen.getArmor());
        System.out.println(garen.getmoveSpeed());
        System.out.println(teemo.getHp());

    }
}



