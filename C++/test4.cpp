#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;
int main ()
{
    int i,j;

    //��������
    srand((unsigned)time(NULL));

    /*����ʮ�������*/
    for(i=0;i<10;i++)
    {
        //����ʵ�ʵ������
        //����� = rand()%(���ֵ - ��Сֵ +1) + ��Сֵ;
        j=rand() % (5000 - 500 + 1) + 500;
        cout << "�������"<< j << endl;
    }

    return 0;
}