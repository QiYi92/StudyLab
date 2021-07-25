package com.study.Array6;

public class 增强for循环训练_6
{
    public static void main(String[] args)
    {
        int[] a = new int[5]; //随机数容器
        int answer = 0; //答案容器
        //增强for循环只能用于取值，不能用来修改数值里的值
        for (int i=0; i<a.length;i++)
        {
            a[i] = (int)(Math.random()*100);
            System.out.print(a[i]+" ");
        }


        System.out.print("\n"+"最大的数是：");
        for (int biggest : a)
        {
            if (answer < biggest)
                answer = biggest;
        }
        System.out.print(answer);
    }
}
