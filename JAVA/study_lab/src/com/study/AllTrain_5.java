package com.study;

public class AllTrain_5
{
    public static void main(String[] args)
    {
        int i,j;
        float l = 0.681f; //分割率的值
        final ans;
        for(i = 0;i<=20;i++)
        {
            for(j = 0;j<=20;j++)
            {
                if(i%2==0 && j%2==0)
                    continue;
                float value = i/j;
                float Dvalue = value-l; //差值
                Dvalue = Dvalue < 0 ? 0-Dvalue:Dvalue; //取绝对值

                if ()


            }
        }
        System.out.println("黄金分割点（0.618）最近两个数相处是"+i+"/"+j+"="+ans);
    }
}
