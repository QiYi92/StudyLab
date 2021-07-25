package com.study.Array6;
//增强for循环
public class 增强for循环_6
{
    public static void main(String[] args)
    {
        int[] values = new int[]{18,62,68,82,65,9};
        //常规遍历
        for (int i = 0;i < values.length;i++)
        {
            int each = values[i];
            System.out.println(each);
        }

        //增强型for循环遍历
        for (int each : values)
        {
            System.out.println(each);
        }
    }

}
