package com.study;

import java.util.Scanner;

public class CountTrain_4
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in); //输入
        int a = s.nextInt();
        System.out.println("第一个整数："+a);
        int b = s.nextInt();
        System.out.println("第二个整数："+b);

        System.out.println("比较"+a+">"+b+":"+(a>b));
        System.out.println("比较"+a+">="+b+":"+(a>=b));
        System.out.println("比较"+a+"<"+b+":"+(a<b));
        System.out.println("比较"+a+"<="+b+":"+(a<=b));
        System.out.println("比较"+a+"=="+b+":"+(a==b));
        System.out.println("比较"+a+"!="+b+":"+(a!=b));
    }
}
