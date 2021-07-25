package com.study.Class_And_Object7;

public class This
{
    String name; //姓名

    float hp; //血量

    float armor; //护甲

    int moveSpeed; //移动速度

    //打印内存中的虚拟地址
    public void showAddressInMemory()
    {
        System.out.println("打印this看到的虚拟地址："+ this);
    }

    public static void main(String[] args) {
        This garen =  new This();
        garen.name = "盖伦";
        //直接打印对象，会显示该对象在内存中的虚拟地址
        //格式：Hero@c17164 c17164即虚拟地址，每次执行，得到的地址不一定一样

        System.out.println("打印对象看到的虚拟地址："+ garen);
        //调用showAddressInMemory，打印该对象的this，显示相同的虚拟地址
        garen.showAddressInMemory();

        This teemo =  new This();
        teemo.name = "提莫";
        System.out.println("打印对象看到的虚拟地址："+ teemo);
        teemo.showAddressInMemory();
    }
}
