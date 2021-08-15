package com.study.Train10;

// 根据UML类创建pet（宠物）接口
public interface Pet
{
    // 提供setName(String name) 为该宠物命名
    void setName(String name);

    // 提供getName() 返回该宠物的名字
    String getName();

    // 提供 play()方法
    void play();
}
