package com.study;
import java.util.Scanner;
public class ifTrain_5
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("请输入身高（m）");
        int m = s.nextInt(); //身高
        System.out.println("请输入体重（kg）");
        int kg = s.nextInt(); //体重
        int bmi = kg / (m * m);
        if (bmi < 18.5)
            System.out.println("身体状态是：体重过轻");
        else if(bmi > 18.5 && bmi < 24)
            System.out.println("身体状态是：正常范围");
        else if(bmi > 24 && bmi < 27)
            System.out.println("身体状态是：体重过重");
        else if(bmi > 27 && bmi < 30)
            System.out.println("身体状态是：轻度肥胖");
        else if(bmi > 30 && bmi <35)
            System.out.println("身体状态是：中度肥胖");
        else if(bmi >= 35)
            System.out.println("身体状态是：重度肥胖");

    }
}
