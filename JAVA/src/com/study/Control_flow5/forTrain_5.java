package com.study.Control_flow5;

public class forTrain_5
{
    public static void main(String[] args)
    {
        //天朝有一个乞丐姓洪，去天桥要钱
        //第一天要了1块钱
        //第二天要了2块钱
        //第三天要了4块钱
        //第四天要了8块钱
        //以此类推
        //
        //问题： 洪乞丐干10天，收入是多少？
        int money = 0;
        int day=10;
        int sum=0;
        for(int i=1;i<=day;i++)
        {
            if(money==0)
                money = 1;
            else
                money *= 2;
            sum+=money;
            System.out.println("干了"+(i)+"天,收入"+sum+"块钱");
        }
    }
}
