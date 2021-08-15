package com.study.Train10;

// Spider继承Animal类
public class Spider extends Animal
{
    @Override
    // 定义默认构造器，它调用父类构造器来指明所有蜘蛛都是8条腿
    //实现eat方法
    public void eat()
    {
        // 实现eat方法
        System.out.println("spider eating");
    }
    // 定义默认构造器，它调用父类构造器来指明所有蜘蛛都是8条腿
    public Spider()
    {
        // 调用父类的构造方法
        super(8);
    }

}
