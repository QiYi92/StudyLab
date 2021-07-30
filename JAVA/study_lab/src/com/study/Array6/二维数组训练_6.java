package com.study.Array6;

public class 二维数组训练_6
{
    public static void main(String[] args)
    {
        int max = 0; //最大值容器
        int b = 0; //最大值坐标
        int c = 0; //最大值坐标
        int[][] a = new int[5][5];
        for (int i = 0;i< a.length;i++)
        {
            for (int j = 0;j< a[0].length;j++)
            {
                //取100以内随机数
                a[i][j] = (int)(Math.random()*100);
                if (a[i][j]>max)
                {
                    max = a[i][j];
                    b = i;
                    c = j;
                }
                System.out.print(a[i][j]+"\t");
            }
            System.out.println();
        }
        System.out.println("最大值为"+max+"\n其坐标为：("+b+","+c+")");
    }
}
