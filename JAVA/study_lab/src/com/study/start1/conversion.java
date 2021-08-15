package com.study.start1;

public class conversion
{
    public static void main(String[] arg) {
        char c = 'A';
        short s = 80;
        //虽然short和char都是16位
        //互相转换需要强制进行
        c = (char) s;
        // s = c直接转换会编译错误

        //低精度 转 高精度
        long l = 50;
        int i = 50;
        //int低精度转long高精度，直接转就行了
        l = i;

        //高精度 转 低精度
        //b的类型是byte,其长度是8，最大只能放127
        //i1 的类型是int, 其长度是32,最大，反正就是很大了，超过127
        //所以， 把int类型的数据转成为byte类型的数据，是有风险的
        //有的时候是可以转换的，比如 b = i1 (i1=10);
        //有的时候不可以转换 比如 b= i2 (i2=300) 因为放不下了
        //编译器就会提示错误
        //只能采用强制转换
        byte b = 5;
        int i1 = 10;
        int i2 = 300;

        b = (byte) i1;
        //因为i1的值是在byte范围之内，所以即便进行强制转换
        //最后得到的值，也是10
        System.out.println(b);

        //因为i2的值是在byte范围之外，所以就会按照byte的长度进行截取
        //i2的值是300，其对应的二进制数是 100101100
        //按照byte的长度8位进行截取后，其值为 00101100 即44
        b = (byte) i2;
        System.out.println(b);

        //查看一个整数对应的二进制数
        System.out.println(Integer.toBinaryString(i2));

        //类型转换练习
        //整型和整型进行运算的时候，如果两边的值都是小于或者等于int的，那么其结果就是int
    }
    public void method1(final int j)
    {
        short aa = 1;
        short bb = 2;
        short cc = (short) (aa + bb);
        System.out.println(cc);
    }
}
