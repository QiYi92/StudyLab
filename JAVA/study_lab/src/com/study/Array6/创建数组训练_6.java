package com.study.Array6;

public class 创建数组训练_6
{
    public static void main(String[] args)
    {
        int[] a = new int[5];
        // 0-100内随机整数获取方法之一 (int)(Math.random()*100)
        a[0] = (int)(Math.random() * 100);
        a[1] = (int)(Math.random() * 100);
        a[2] = (int)(Math.random() * 100);
        a[3] = (int)(Math.random() * 100);
        a[4] = (int)(Math.random() * 100);

        System.out.println("数组中的各个随机数是:");
        for(int i = 0; i<a.length; i++)
            System.out.println(a[i]);

        System.out.println("本练习的目的是，找出最小的一个值:");
    }
}
