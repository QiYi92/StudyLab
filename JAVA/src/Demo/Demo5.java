package Demo;

public class Demo5
{
    public static void main(String[] args)
    {
        int sum = 0,b = 0;
        for (int i = 1;i <= 10;i++)
        {
            b = b * 10 + 8;
            sum += b;
        }
        System.out.println(sum);
    }
}
