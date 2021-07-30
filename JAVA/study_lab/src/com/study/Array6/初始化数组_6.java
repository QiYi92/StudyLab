package com.study.Array6;

public class 初始化数组_6
{
    public static void main(String[] args)
    {
        //分配空间
        int[] a = new int[5];
        //赋值
        a[0] = 100;
        a[1] = 101;
        a[2] = 103;
        a[3] = 120;
        a[4] = 140;

        //分配空间同时赋值,方法一
        int[] b = new int[]{100,102,444,836,3235};

        //分配空间同时赋值，方法二
        int[] c = {100,102,444,836,3235};

    }
}
