package com.study;

public class AllTrain_5
{
    public static void main(String[] args)
    {
        //思路：寻找两个数相除，其结果离黄金分割点0.618最近
        //分子和分母不能同时为偶数
        //分子和分母的取值范围在1-20
        int range = 20; //取值范围
        float minDiff = 100; //离黄金分割率点的差值
        float breakPoint = 0.618f; // 黄金分割率
        int answerFenzi = 0; // 找到的分子
        int answerFenmu = 0; // 找到的分母
        for(int fenzi = 1;fenzi <= range; fenzi++)
        {
            for(int fenmu = 1;fenmu <= range;fenmu++)
            {
                // 分子分母不能同时为偶数
                if(0 == fenzi % 2 & 0 == fenmu %2)
                    continue;
                // 取值
                float value = (float) fenzi/fenmu;
                // 取黄金分割率差值
                float diff = value - breakPoint;
                // 绝对值
                diff = diff < 0 ? 0 - diff : diff; //如果diff小于0，则负负得正取正值

                //找出最小的差值
                if(diff < minDiff)
                {
                    minDiff = diff;
                    answerFenzi = fenzi;
                    answerFenmu = fenmu;
                }

            }
        }
        System.out.println("离黄金分割点（"+ breakPoint +"）最近的两个数相除是："+ answerFenzi +"/" + answerFenmu + "=" + ((float)answerFenzi/answerFenmu));


    }
}
