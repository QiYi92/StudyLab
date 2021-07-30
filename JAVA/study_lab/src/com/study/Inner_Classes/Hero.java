package com.study.Inner_Classes;

public class Hero
{
    public String name; //姓名

    private float hp; //血量

    int moveSpeed; //移动速度


    private static void battleWin()
    {
        System.out.println("battle win");
    }

    public void attack() {
    }

    //敌方的水晶 (static静态声明)
    static class EnemyCrystal
    {
        int hp = 5000;

        //如果水晶血量0.则宣布胜利
        public void checkIfVictory()
        {
            if (hp == 0)
            {
                Hero.battleWin();

                //静态内部类不能直接访问外部类的对象属性
                // !!!取消注释会报错: 无法从 static 上下文引用非 static 字段 'name'
                //System.out.println(name +"win this game");
            }
        }
    }


    // 非静态内部类，只有一个外部类对象存在的时候，才有意义
    // 战斗成绩只有在一个英雄对象存在的时候才有意义

    class BattleScore
    {
        int kill;
        int die;
        int assit;

        public void legendary()
        {
            if(kill >= 8)
                System.out.println(name + "超神！");
            else
                System.out.println(name + "尚未超神！");
        }
    }

    public static void main(String[] args)
    {
        Hero garen = new Hero();
        garen.name = "盖伦";
        // 实例化内部类
        // BattleScore对象只有在一个英雄对象存在的时候才有意义
        // 所以其实例化必须建立在一个外部类对象的基础之上

        //BattleScore内部类对象score建立在外部类Hero的对象garen上
        //语法: new 外部类().new 内部类()
        BattleScore score = garen.new BattleScore();

        score.kill = 9;
        score.legendary();

        //实例化静态内部类
        //语法new 外部类.静态内部类();
        Hero.EnemyCrystal crystal = new Hero.EnemyCrystal();
        crystal.checkIfVictory();
    }
}
