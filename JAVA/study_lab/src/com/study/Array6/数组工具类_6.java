package com.study.Array6;

import java.util.Arrays;
public class 数组工具类_6
{
    public static void main(String[] args)
    {
        //数组复制 Arrays.copyOfRange()
        int[] a = new int[]{18,54,89,56,92};
        // copyOfRange(源数组，起始位置，结束位置)
        // 第一个参数表示源数组
        // 第二个参数表示开始位置(取得到)
        // 第三个参数表示结束位置(取不到)
        int[] b = Arrays.copyOfRange(a,0,3);
        System.out.print("数组c的内容："+"\n"+Arrays.toString(b));


        //字符串转换 Arrays.toString()
        int[] c = new int[]{14,56,85,56,9};
        String content = Arrays.toString(c);
        System.out.println(content);


        //排序 Arrays.sort()
        int[] d = new int[]{34,56,78,90,9,84};
        System.out.println("排序之前 :");
        System.out.println(Arrays.toString(d));
        //排序函数
        Arrays.sort(d);
        System.out.println("排序之后:");
        System.out.println(Arrays.toString(d)+"\n");


        //搜索 Arrays.binarySearch(数组,需要搜索的值 )
        int[] e = new int[]{23,45,67,89,79};
        //先排序
        Arrays.sort(e);
        System.out.println(Arrays.toString(e));
        //使用binarySearch之前，必须先使用sort进行排序
        System.out.println("数字67出现的位置:"+Arrays.binarySearch(e, 67)+"\n");


        //判断是否相同 Array.equals(数组A,数组B)
        int[] f = new int[] { 18, 62, 68, 82, 65, 9 };
        int[] g = new int[] { 18, 62, 68, 82, 65, 8 };

        System.out.println("f,g两数组是否相同："+Arrays.equals(f,g)+"\n");

        //填充 Array.fill(数组，值)
        int[] h = new int[10];
        //使用同一个值，填充整个数组
        Arrays.fill(h,5);
        System.out.println(Arrays.toString(h));

    }
}
