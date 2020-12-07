#include <iostream>
using namespace std;

class printData
{
    public:
       void print(int i){
           cout << "整数为:" << i << endl;
       }

       void print(double f){
           cout << "浮点数为:" << f << endl;
       }

       void print(char c[]){
           cout << "字符串为:" << c << endl;
       }
};

int main(void)
{
    printData pd;
    // 输出整数
    pd.print(7);
    // 输出浮点数
    pd.print(53.215);
    // 输出字符串
    char c[] = "啥玩意";
    pd.print(c);

    return 0;


}
