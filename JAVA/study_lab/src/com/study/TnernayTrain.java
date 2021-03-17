package com.study;
import java.util.Scanner;
public class TnernayTrain
{
    public static void main(String[] arg)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("今天是周几");
        int day = s.nextInt();
        String status = day >= 6?"周末":"工作日";
        System.out.println("今天是"+status);
    }
}
