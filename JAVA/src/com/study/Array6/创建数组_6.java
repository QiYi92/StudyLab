package com.study.Array6;

public class 创建数组_6
{
    public static void main(String[] args)
    {   //声明一个引用
        int[] a;
        //创建一个长度是5的数组，并且使用引用a指向该数组,范围是[1-4]
        a = new int[5];

        System.out.println(a.length); //打印数组长度
        a[4] = 100;
        //a[5] = 101;

        int [] b = new int[5]; //声明的同时，指向一个数组
    }
}
