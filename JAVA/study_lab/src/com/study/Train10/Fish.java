package com.study.Train10;

public class Fish extends Animal implements Pet
{
    private String name;
    protected Fish()
    {
        super(0);
    }
    // 验证@Override下面的方法名是否是你父类中所有的，如果没有则报错
    @Override
    public void eat()
    {
        System.out.println("Fish is eating");
    }

    public void walk()
    {
        System.out.println("swimming");
    }

    @Override
    public void setName(String name)
    {
        // TODO Auto-generated method stub
        this.name = name;
    }

    @Override
    public String getName()
    {
        // TODO Auto-generated method stub
        return this.name;
    }

    @Override
    public void play() {
        // TODO Auto-generated method stub
        System.out.println("playing");
    }
}
