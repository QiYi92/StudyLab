package com.study.Control_flow5;

public class breakTrain_5
{
    public static void main(String[] args)
    {
        int fundPerMonth = 1000;
        int fundPerYear = fundPerMonth * 12;
        float rate = 0.20f; //年利率
        //复利公式 F=p*((1+r)^n)
        int sum = 0;
        int target = 1000*1000; //目标
        for(int j =1;j<100;j++)
        {
            int year = j;
            float F_rate = 1;
            for (int i = 0;i<year;i++)
            {
                F_rate=F_rate*(1+rate);
            }
            int F=(int)(fundPerYear*F_rate);
            sum += F;
            System.out.println("经过" + year + " 年， 总收入 " + sum);
            if (sum>=target)
            {
                System.out.println("一共需要" + year + "年，累计收入超过" + target );
                break;
            }

        }
    }
}
