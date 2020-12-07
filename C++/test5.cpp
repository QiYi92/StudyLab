#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

int main ()
{
    int n[10]; //创建一个包含10个整数的数组

    //初始化数组元素
    for(int i=0;i<10;i++)
    {
        n[i] = i + 100; //设置元素i为i+100
    }
    /*Element和Value之间空13格*/
    cout << "Element" << setw(13) << "Value" <<endl;
    
    for(int j=0;j<10;j++)
    {
        cout << setw(7) << j << setw(13) << n[j] <<endl;
    }


    return 0;
}