package com.study;

public class Logic_4
{
    //长路与短路

    //无论长路与还是短路与
    //两边的运算单元都是布尔值
    //都为真时，才为真
    //任意为假，就为假
    //区别
    //长路与 两侧，都会被运算
    //短路与 只要第一个是false，第二个就不进行运算了

    public static void main(String[] args)
    {
        // "&&"
        //长路与  无论第一个表达式的值是true或者false,第二个的值，都会被运算
        int i = 2;
        System.out.println(i == 1 & i++ ==2);
        //无论如何i++都会被执行，所以i的值变成了3
        System.out.println(i);

        //短路与只要第一个表达式的值是false的，第二个表达式的值，就不需要进行运算了
        int j = 2;
        System.out.println(j==1 && j++ == 2);
        //因为j==1返回false,所以右边的j++就没有执行了，所以j的值，还是2
        System.out.println(j);


        // "||"
        //长路或  无论第一个表达式的值是true或者false,第二个的值，都会被运算
        int k = 2;
        System.out.println( k== 1 | k++ ==2  ); //无论如何i++都会被执行，所以i的值变成了3
        System.out.println(k);

        //短路或 只要第一个表达式的值是true的，第二个表达式的值，就不需要进行运算了
        int l = 2;
        System.out.println( l== 2 || l++ ==2  );  //因为j==2返回true,所以右边的j++就没有执行了，所以j的值，还是2
        System.out.println(l);

        // "取反"
        boolean b = true;
        System.out.println(b); //输出true
        System.out.println(!b);//输出false


        // "异或"
        //异或^
        //不同，返回真
        //相同，返回假

        boolean c = true;
        boolean d = false;

        System.out.println(c^d); //不同返回真
        System.out.println(c^!d); //相同返回假

        //练习
        int i_ = 1;
        boolean b_ = !(i++ == 3) ^ (i++ ==2) && (i++==3);
        System.out.println(b_);
        System.out.println(i_);

    }

}
