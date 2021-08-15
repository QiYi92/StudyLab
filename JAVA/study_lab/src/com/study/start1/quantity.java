package com.study.start1;

public class quantity
{
    public static void main(String[] arg)
    {
        //整型
        byte b = 1; //字节
        short s =200; //短整型
        int i = 300; //int整形
        long l = 400; //长整型
        byte b2 = 127; //byte值<128

        //字符型
        char c = '中'; //char只能存放一个字符，超过一个字符就会编译错误

        //浮点型
        //浮点数类型有两种
        //float 长度为32位
        //double 长度为64位
        //注意： 默认的小数值是double类型的
        //所以 float f = 54.321会出现编译错误，因为54.321的默认类型是 double，其类型 长度为64，超过了float的长度32
        //在数字后面加一个字母f，直接把该数字声明成float类型
        //float f2 = 54.321f,
        //这样就不会出错了
        double d =123.45;

        //float f = 54.321; //该行会出现编译错误
        float f2 = 54.321f;

        //布尔型
        boolean b1 = true;
        boolean b3 = false;

        //String并不是基本类型
        String str = "Hello Java";

        //练习
        float train1 = 3.14f;
        double train2 = 2.769343;
        int train3 = 365;
        short train4 = 12;
        char train5 = '吃';
        boolean train6 = false;
        String train7 = "不可描述";

        long val = 26L; //long型
        int decVal = 26; //int型
        int hexVal = 0x1a; //16进制
        int oxVal = 032; //8进制
        int binVal = 0b11010; //2进制

        //当以f或者F结尾的时候，就表示一个float类型的浮点数，否则就是double类型（以d或者D结尾，写不写都可以）。
        //浮点数还可以用E或者e表示（科学计数法）
        //e2表示10的二次方，即100
        //1.234e2 = 1.234x100
        float f1 = 123.4F; //以F结尾的字面值表示float类型
        double d1 = 123.4; //默认double类型
        double d2 = 1.234e2; //科学计数法表示double

        char a = 'c';

        //以下是转义字符
        char tab = '\t'; //制表符
        char carriageReturn = '\r'; //回车
        char newLine = '\n'; //换行
        char doubleQuote = '\"'; //双引号
        char singleQuote = '\''; //单引号
        char backslash = '\\'; //反斜杠

        //练习字面值
        byte _b = 12;
        short _s = 200;
        int _i = 256;
        long _l = 2556500;
        float _f = 123.45f;
        double _d = 25565.25565;
        char _c = 'a';
        String _str = "啊";

    }
}
