package restart;

import java.util.Scanner;
public class Test
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        System.out.println("第一个整数："+a);
        float b = s.nextFloat();
        System.out.println("第二个浮点数："+b);
        String rn = s.nextLine();
        String c = s.nextLine();
        System.out.println("第三个字符串："+c);
    }
}
