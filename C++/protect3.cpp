#include <iostream>

using namespace std;

int main()
{
    int i;
    double c;
    double f;

    cout << "�¶�ת����v0.1" << endl;
    cout << "(1)����ת�����¶�" << endl;
    cout << "(2)����ת�����¶�" << endl;
    cout << "��ѡ��ʹ��ģʽ��������ţ���";
    cin >> i;
    cout << endl;
    if(i==1)
    {
        cout << "�����뻪���¶�:";
        cin >> f; 
        c=(f-32)*5/9;
        cout << "�����¶�Ϊ:" << c << "��" <<endl;
    }
    else if(i==2)
    {
        cout << "�����������¶�:";
        cin >> c; 
        f = c*9/5+32;
        cout << "�����¶�Ϊ:" << f << "�H" <<endl;
    }
    else
    {
        cout << "�����쳣" <<endl;
    }
    return 0;
}