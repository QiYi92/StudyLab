package com.study.Array6;
//选择排序
public class 选择排序_6
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
        //选择排序
        for (int j = 0; j < a.length-1; j++)
        {
            for (int i = j+1; i<a.length; i++)
            {
                if(a[i]<a[j])
                {
                    int temp = a[j];
                    a[j] = a[i];
                    a[i] = temp;
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
