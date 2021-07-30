package com.study.Date10;

//字符串转日期
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
public class TestDate2
{
    public static void main(String[] args)
    {
        SimpleDateFormat sdf =new SimpleDateFormat("yyyy/MM/dd HH:mm:ss" );

        String str = "2021/1/5 12:12:12";
        try
        {
            Date d = sdf.parse(str);
            System.out.printf("字符串 %s 通过格式  yyyy/MM/dd HH:mm:ss %n转换为日期对象: %s",str,d.toString());
        }catch (ParseException e)
        {
            //TODO 自动生成的catch模块
            e.printStackTrace();
        }
    }

}
