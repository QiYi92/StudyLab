package com.study.Control_flow5;

public class AllTrain2_5
{
    public static void main(String[] args)
    {
        //水仙花数
        for(int i = 100;i < 1000;i++)
        {
            int baiwei = i / 100;
            int shiwei = i / 10 % 10;
            int gewei = i % 10;
            int cube = (int)(Math.pow(baiwei,3)+(Math.pow(shiwei,3))+(Math.pow(gewei,3)));
            if(cube == i)
            {
                System.out.println("找到水仙花数："+ i);
            }
        }
    }

}
