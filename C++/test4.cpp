#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;
int main ()
{
    int i,j;

    //设置种子
    srand((unsigned)time(NULL));

    /*生成十个随机数*/
    for(i=0;i<10;i++)
    {
        //生成实际的随机数
        //随机数 = rand()%(最大值 - 最小值 +1) + 最小值;
        j=rand() % (5000 - 500 + 1) + 500;
        cout << "随机数："<< j << endl;
    }

    return 0;
}