package com.study.Array6;
import java.util.Arrays; //java标准库提供的Arrays.toString()

public class 数组复制训练_6
{
    public static void main(String[] args)
    {
        //(int)(Math.random()*5+5)是取5-10之间的整数
        int[] a = new int[(int)(Math.random()*5+5)];
        int[] b = new int[(int)(Math.random()*5+5)];
        int[] c = new int[a.length+b.length];

        //b数组的循环
        for (int i = 0;i<a.length;i++)
        {
            a[i] = (int)(Math.random()*100);
        }
        //a数组的循环
        for (int i = 0;i<b.length;i++)
        {
            b[i] = (int)(Math.random()*100);
        }

        //复制a b 数组至c
        System.arraycopy(a, 0, c, 0, a.length);
        System.arraycopy(b, 0, c, a.length, b.length);

        //利用java标准库提供的Arrays.toString()
        //输出整个数组
        System.out.println("数组a的内容："+"\n"+Arrays.toString(a));
        System.out.println("数组b的内容："+"\n"+Arrays.toString(b));
        System.out.println("数组c的内容："+"\n"+Arrays.toString(c));
    }
}
