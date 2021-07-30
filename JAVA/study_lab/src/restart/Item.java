package restart;

public class Item
{
    //item类属性
    String name;
    int price;

    public static void main(String[] args)
    {
        //创建对象物品
        Item blood_vial = new Item();
        blood_vial.name = "血瓶";
        blood_vial.price = 50;

        Item grass_shoes = new Item();
        grass_shoes.name = "草鞋";
        grass_shoes.price = 300;

        Item long_sword = new Item();
        long_sword.name = "长剑";
        long_sword.price = 350;



    }
}
