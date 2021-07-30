package Demo;

public class Demo3
{
    public static void main(String[] args)
    {
        double sum = 0,a=1;
        int i = 1;
        //for循环
        for( ;i<=20;i++)
        {
            sum = sum + a;
            a = a * (1.0/i);
        }
        System.out.println(sum);

    }
}
