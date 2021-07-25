package com.study.Array6;
//冒泡排序

public class 冒泡排序_6
{
    public static void main(String[] args)
    {
        int[] a = new int[]{18,62,68,82,65,9};
        //排序前，先把内容打印出来
        for (int i=0;i<a.length;i++)
        {
            System.out.print(a[i] + " ");
        }
        System.out.println(" ");

        for (int j = 0; j<a.length; j++)
        {
            for (int i = 0; i<a.length-j-1; i++)
            {
                if (a[i] > a[i+1])
                {
                    int temp = a[i];
                    a[i] = a[i+1];
                    a[i+1] = temp;
                }
            }
        }
        //排序后打印内容
        for (int i = 0;i < a.length; i++)
        {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}
