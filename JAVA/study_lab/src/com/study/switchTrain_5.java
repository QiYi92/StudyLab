package com.study;
import java.util.Scanner;
public class switchTrain_5
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int month = s.nextInt();
        switch(month)
        {
            case 3:
            case 4:
            case 5:
                System.out.println(month+"月是春季");
                break;
            case 6:
            case 7:
            case 8:
                System.out.println(month+"月是夏季");
                break;
            case 9:
            case 10:
            case 11:
                System.out.println(month+"月是秋季");
                break;
            case 12:
            case 1:
            case 2:
                System.out.println(month+"月是冬季");
                break;
        }
//        //增强switch
//        Scanner s = new Scanner(System.in);
//        int month = s.nextInt();
//        switch (month)
//        {
//            case 3, 4, 5 -> System.out.println(month + "月是春季");
//            case 6, 7, 8 -> System.out.println(month + "是夏季");
//            case 9, 10, 11 -> System.out.println(month + "是秋季");
//            case 12, 1, 2 -> System.out.println(month + "是冬季");
//        }
    }
}
