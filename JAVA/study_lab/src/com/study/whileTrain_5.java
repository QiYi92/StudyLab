package com.study;
import java.util.Scanner;
public class whileTrain_5
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int ans = 1;
        int i = 0;
        while (i!=num)
        {
            ans *= num-i;
            i++;
        }
        System.out.println(ans);
    }
}
