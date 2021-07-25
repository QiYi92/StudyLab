package Demo;

public class Demo1
{
    public static void main(String[] args)
    {
        int sum = 0;
        for (int i = 1;i <= 10;i++)
        {
            int a = 1;
            for (int j = i;j >= 1;j--)
            {
                a = a * j;
            }
            sum += a;
        }
        System.out.println(sum);
    }
}
