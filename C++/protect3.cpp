#include <iostream>

using namespace std;

int main()
{
    int i;
    double c;
    double f;

    cout << "温度转换器v0.1" << endl;
    cout << "(1)华氏转摄氏温度" << endl;
    cout << "(2)摄氏转华氏温度" << endl;
    cout << "请选择使用模式（输入序号）：";
    cin >> i;
    cout << endl;
    if(i==1)
    {
        cout << "请输入华氏温度:";
        cin >> f; 
        c=(f-32)*5/9;
        cout << "摄氏温度为:" << c << "℃" <<endl;
    }
    else if(i==2)
    {
        cout << "请输入摄氏温度:";
        cin >> c; 
        f = c*9/5+32;
        cout << "华氏温度为:" << f << "℉" <<endl;
    }
    else
    {
        cout << "输入异常" <<endl;
    }
    return 0;
}