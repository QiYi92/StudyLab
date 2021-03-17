package com.study;
import java.util.Scanner;
public class ScannerTrain
{
    //使用Scanner类，需要在最前面加上import java.util.Scanner;
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        System.out.println("第一个整数："+a);
        int b = s.nextInt();
        System.out.println("第二个整数："+b);


        float c = s.nextFloat();
        System.out.println("读取的浮点数值是："+c);

        String d = s.nextLine();
        System.out.println("读取的字符串是："+d);

        //需要注意的是，如果在通过nextInt()读取了整数后，再接着读取字符串，读出来的是回车换行:"\r\n",因为nextInt仅仅读取数字信息，而不会读取回车换行"\r\n".
        //
        //所以，如果在业务上需要读取了整数后，接着读取字符串，那么就应该连续执行两次nextLine()，第一次是取走回车换行，第二次才是读取真正的字符串
        int i = s.nextInt();
        System.out.println("读取的整数是："+i);
        String rn = s.nextLine();
        String p = s.nextLine();
        System.out.println("读取的字符串是："+p);
    }
}
