package com.study.Control_flow5;

public class booleanTrain_5
{
    public static void main(String[] args)
    {
        //是否终止外部循环
        boolean breakout = false;
        for(int i = 0;i < 10;i++)
        {
            for (int j = 0; j < 10; j++)
            {
                System.out.println(i+":"+j);
                if(0==j%2)
                {
                    breakout = true;
                    break;
                }
            }
            if(breakout) //判断是否终止外部循环
                break;
        }

        outloop: //outloop判定表示
        for(int x = 0;x<10;x++)
        {
            for (int y = 0;y<10;y++)
            {
                System.out.println(x+":"+y);
                if(0==y%2)
                    break outloop; //如果是双数，结束外部循环
            }
        }

    }
}
