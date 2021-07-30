package Demo;

public class Demo2
{
    public static void main(String args[])
    {
        for (int n = 2;n <= 100;n++)
        {
            boolean x = true; //触发器
            for (int i = 2; i < n; i++)
            {
                if (n%i==0)
                    x = false;
                    break;
            }
            if(x)
            {
                System.out.println(n);
            }
        }

    }

}
