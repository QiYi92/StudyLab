#include <iostream>
using namespace std;

class printData
{
    public:
       void print(int i){
           cout << "����Ϊ:" << i << endl;
       }

       void print(double f){
           cout << "������Ϊ:" << f << endl;
       }

       void print(char c[]){
           cout << "�ַ���Ϊ:" << c << endl;
       }
};

int main(void)
{
    printData pd;
    // �������
    pd.print(7);
    // ���������
    pd.print(53.215);
    // ����ַ���
    char c[] = "ɶ����";
    pd.print(c);

    return 0;


}
