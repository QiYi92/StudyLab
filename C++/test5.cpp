#include <iostream>
using namespace std;

#include <iomanip>
using std::setw;

int main ()
{
    int n[10]; //����һ������10������������

    //��ʼ������Ԫ��
    for(int i=0;i<10;i++)
    {
        n[i] = i + 100; //����Ԫ��iΪi+100
    }
    /*Element��Value֮���13��*/
    cout << "Element" << setw(13) << "Value" <<endl;
    
    for(int j=0;j<10;j++)
    {
        cout << setw(7) << j << setw(13) << n[j] <<endl;
    }


    return 0;
}