package com.study.Train10;

public class Cat extends Animal implements Pet
{
    private String name;

    // 定义一个构造器，它使用String参数指定猫的名字；该构造器必须调用超类构造器来指明所有的猫都是四条腿。
    public Cat(String name)
    {
        super(4);
        this.name = name;
    }

    // 另定义一个无参的构造器。该构造器调用前一个构造器（用this关键字）并传递一个空字符串作为参数
    public Cat()
    {
        this("");
    }
    @Override
    public void setName(String name)
    {
        this.name = name;
    }

    @Override
    public String getName()
    {
        // TODO Auto-generated method stub
        return name;
    }

    @Override
    public void play() {
        System.out.println("Cat is playing");
    }
    // 实现eat方法
    @Override
    public void eat()
    {
        System.out.println("eating");
    }
}
