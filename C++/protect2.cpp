#include <iostream>
#include <conio.h>
#include <string>
using namespace std;

class student
{
    private:
        long xh; //ѧ�����
        char mz[10]; //ѧ������
        char xb[2]; //ѧ���Ա�
        char zy[40]; //רҵ����
        char bj[10]; //�༶����
        char nj[10]; //�꼶����
        char dz[40]; //��ͥסַ
        long dh; //�绰����
    public:
        void cinnumber()
        {
            cout << "������ѧ�����";
            cin >> xh;
            cout << endl;

            cout << "������ѧ������";
            cin >> mz;
            cout << endl;

            cout << "������ѧ���Ա�";
            cin >> xb;
            cout << endl;

            cout << "������רҵ����";
            cin >> zy;
            cout << endl;

            cout << "������༶";
            cin >> bj;
            cout << endl;

            cout << "�������꼶";
            cin >> nj;
            cout << endl;

            cout << "�������ͥסַ";
            cin >> dz;
            cout << endl;

            cout << "������绰����";
            cin >> dh;
            cout << endl;
        }

        void coutnumber()
        {
            cout << "ѧ����Ϣ��" << endl;
            cout << "ѧ�����:" << xh <<endl;
            cout << "ѧ������:" << mz <<endl;
            cout << "ѧ���Ա�:" << xb <<endl;
            cout << "רҵ����:" << zy <<endl;
            cout << "�༶:" << bj <<endl;
            cout << "�꼶:" << nj <<endl;
            cout << "��ͥסַ" << dz << endl;
            cout << "�绰����" << dh << endl;
        }
};

int main()
{
    student s1;
    s1.cinnumber();
    s1.coutnumber();
    return 0;
}
