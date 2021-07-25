package com.study.Control_flow5;
import java.util.Scanner;
public class ifTrain2_5
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int year = s.nextInt();
        if(year % 4 ==0 && year % 100 != 0)
            System.out.println(year+"是闰年");
        else if(year % 400 == 0)
            System.out.println(year+"是闰年");
        else
            System.out.println(year+"不是闰年");

    }
}
