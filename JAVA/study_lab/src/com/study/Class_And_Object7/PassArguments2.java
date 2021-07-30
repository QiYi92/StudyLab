package com.study.Class_And_Object7;

public class PassArguments2
{
    String name; // 姓名

    float hp; // 血量

    float armor; // 护甲

    int moveSpeed; // 移动速度

    public PassArguments2(String name, float hp) {
        this.name = name;
        this.hp = hp;
    }

    // 攻击一个英雄，并让他掉damage点血
    public void attack(PassArguments2 hero, int damage) {
        hero.hp = hero.hp - damage;
    }

    public static void main(String[] args) {
        PassArguments2 teemo = new PassArguments2("提莫", 383);
        PassArguments2 garen = new PassArguments2("盖伦", 616);
        garen.attack(teemo, 100);
        System.out.println(teemo.hp);
    }
}
