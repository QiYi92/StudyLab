package com.study.Class_And_Object7;

import restart.Hero;

//引用
public class Quote_7
{
    String name; //姓名
    float hp; //血量
    float armor; //护甲
    int moveSpeed; //移动速度
    public static void main(String[] args)
    {
        //创建一个对象
        new Hero();

        Hero h = new Hero();


        //使用一个引用来指向这个对象
        Hero h1 = new Hero();
        Hero h2 = h1;  //h2指向h1所指向的对象
        Hero h3 = h1;
        Hero h4 = h1;
        Hero h5 = h4;

        //h1,h2,h3,h4,h5 五个引用，都指向同一个对象
    }
}
