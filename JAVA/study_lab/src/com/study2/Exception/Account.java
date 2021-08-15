package com.study2.Exception;

public class Account
{
    // 余额
    protected double balance;

    // 开户存钱
    public  Account(double balance)
    {
        this.balance = balance;
    }

    // 获取当前余额
    public double getBalance()
    {
        return balance;
    }

    // 存钱的数量
    public void deposit(double amt)
    {
        this.balance+=amt;
    }

    //取钱
    public void withdraw(double amt) throws OverDraftException
    {
        //判断银行存的钱是否小于要取的钱数
        if (this.balance<amt)
            // 创建并抛出异常
            // 对应OverDraftException中的 OverDraftException(String msg,double deficit)
            throw new OverDraftException("余额不足",amt-this.balance);
        // 余额足就扣钱
        this.balance -= amt;
    }

    public static void main(String[] args)
    {
        //开户存了1000
        Account a = new Account(1000);
        //存钱1000
        a.deposit(1000);
        //查看余额
        System.out.println(a.getBalance());

        try {
            //取2001
            a.withdraw(2001);
        } catch (OverDraftException e) {
            System.err.println("透支金额："+e.getDeficit());
            e.printStackTrace();
        }

    }


}
