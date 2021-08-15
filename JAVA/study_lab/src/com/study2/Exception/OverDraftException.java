package com.study2.Exception;

// 超支异常
public class OverDraftException extends Exception
{
    private double deficit;

    public double getDeficit()
    {
        return deficit;
    }

    public OverDraftException(String msg,double deficit)
    {
        // 调用父类的构造方法
        super(msg);
        this.deficit = deficit;
    }
}
