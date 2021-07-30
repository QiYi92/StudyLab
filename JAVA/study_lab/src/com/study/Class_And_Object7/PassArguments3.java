package com.study.Class_And_Object7;

public class PassArguments3
{
    String name; //姓名

    float hp; //血量

    float armor; //护甲

    int moveSpeed; //移动速度

    public PassArguments3(){}

    public PassArguments3(String name,float hp)
    {
        this.name = name;
        this.hp = hp;
    }

    //复活
    public void revive(PassArguments3 h)
    {
        //创建的是新的对象，与原有的对象无关
        h = new PassArguments3("提莫",389);
    }

    public static void main(String[] args)
    {
        PassArguments3 teemo = new PassArguments3("提莫",389);

        //受到400伤害，死了
        teemo.hp = teemo.hp - 400;

        //teemo引用，还是指向原来的对象
        teemo.revive(teemo);
        System.out.println(teemo.hp);
    }
}
