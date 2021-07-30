package com.study.Array6;

public class 数组复制_6
{
    public static void main(String[] args)
    {
        int[] a = new int[]{12,23,34,45,56,67};

        int[] b = new int[3]; //并未赋值

        //方法1：for循环
        //方法2：System.arraycopy(源数组,源起始位置,目标数组,目标起始位置,复制长度)
        System.arraycopy(a,0,b,0,3);

        for (int i : b)
        {
            System.out.print(i+" ");
        }

    }
}
