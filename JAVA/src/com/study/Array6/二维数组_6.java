package com.study.Array6;
import java.util.Arrays;

public class 二维数组_6
{
    public static void main(String[] args)
    {
        //初始化二维数组
        int[][] a = new int[2][3]; //有2个一维数组，每个一位数组的长度是3
        a[1][2] = 5; //可以直接访问一维数组

        //只分配二维数组
        int[][] b = new int[2][]; //有两个一维数组，每个一维数组的长度暂未分配
        b[0]  = new int[3]; //必须事先分配长度，才可以访问
        b[0][2] = 5;

        //指定内容的同时，分配空间
        int[][] c = new int[][]
                {
                        {1,2,4},
                        {4,5},
                        {6,7,8,9}
                };
    }
}
