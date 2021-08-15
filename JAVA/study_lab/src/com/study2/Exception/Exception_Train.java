package com.study2.Exception;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
public class Exception_Train
{
    public static int method()
    {
        try
        {
            return return1();
        }
        catch (Exception e)
        {
            return return2();
        }
        finally
        {
            return return3();
        }
    }

    private static int return1() {
        System.out.println("return 1");
        return 1;
    }
    private static int return2() {
        System.out.println("return 2");
        return 2;
    }
    private static int return3() {
        System.out.println("return 3");
        return 3;
    }

    public static void main(String[] args)
    {
        int result = method();
        System.out.println("result:" + result);
    }

}
