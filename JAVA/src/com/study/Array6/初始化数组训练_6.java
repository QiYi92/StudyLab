package com.study.Array6;

public class 初始化数组训练_6
{
    public static void main(String[] args)
    {
        int[] a = new int[5];
        a[0] = (int)(Math.random() * 100);
        a[1] = (int)(Math.random() * 100);
        a[2] = (int)(Math.random() * 100);
        a[3] = (int)(Math.random() * 100);
        a[4] = (int)(Math.random() * 100);

        System.out.print("反转前：");
        for (int i=0;i<a.length;i++)
            System.out.print(a[i]+" ");

        //进行首尾调换
        for (int i = 0;i<a.length/2;i++)
        {
            int middle = a[a.length-i-1]; //将尾部赋值给中转容器
            a[a.length-i-1] = a[i]; //将头部赋值给尾部
            a[i] = middle; //将中转容器赋值给头部
        }

        System.out.print("\n");

        System.out.print("反转后：");
        for (int i=0;i<a.length;i++)
            System.out.print(a[i]+" ");


    }
}
