package com.study.Control_flow5;

public class if_5
{
    public static void main(String[] args)
    {
        boolean b = true;
        if(b)
        {
            System.out.println("yes");
        }
        boolean c = true;
        //如果有多个表达式，必须用大括弧包括起来
        if(c){
            System.out.println("yes1");
            System.out.println("yes2");
            System.out.println("yes3");
        }
        //否则表达式2 3 无论b是否为true都会执行
        if(c)
            System.out.println("yes1");
        System.out.println("yes2");
        System.out.println("yes3");

        //如果只有一个表达式可以不用写括弧，看上去会简约一些
        if(c)
        {
            System.out.println("yes1");
        }
        if(c)
            System.out.println("yes1");

        //if else
        boolean d = false;
        if (d)
            System.out.println("yes");
        else
            System.out.println("no");

        //
        int i = 2;
        if(i==1)
            System.out.println(1);
        if (i==2)
            System.out.println(2);
        if (i==3)
            System.out.println(3);
        if (i==4)
            System.out.println(4);

        //如果使用else if,一旦在53行判断成立，后边判断就不会执行，节约资源
        if (i==1)
            System.out.println(1);
        else if (i==2)
            System.out.println(2);
        else if (i==3)
            System.out.println(3);
        else if (i==4)
            System.out.println(4);


    }
}
