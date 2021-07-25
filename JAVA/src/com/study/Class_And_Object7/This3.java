package com.study.Class_And_Object7;

public class This3
{
    String name; // 姓名

    float hp; // 血量

    float armor; // 护甲

    int moveSpeed; // 移动速度

    // 带一个参数的构造方法
    public This3(String name) {
        System.out.println("一个参数的构造方法");
        this.name = name;
    }

    // 带两个参数的构造方法
    public This3(String name, float hp) {
        this(name);
        System.out.println("两个参数的构造方法");
        this.hp = hp;
    }

    // 带有四个参数的构造方法
    public This3(String name, float hp, float armor, int moveSpeed) {
        this(name,hp); //this()在一个构造方法中调用另一个构造方法
        this.armor = armor;
        this.moveSpeed = moveSpeed;
    }

    public static void main(String[] args) {
        This3 teemo = new This3("提莫", 383);
        System.out.println(teemo.name);
        This3 db =  new This3("死哥",400,27,360);
        System.out.println(db.moveSpeed);
    }
}
