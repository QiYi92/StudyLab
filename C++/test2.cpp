#include <iostream>

// ��������
void func(void); /*�Լ�����ĺ���*/

static int count = 10; /*ȫ�ֱ���*/

int main()
{
    while(count--)
    {
        func();
    }
    return 0;
}
//��������

void func(void)
{
    static int i = 5; // �ֲ���̬����
    i++;
    std::cout << "����iΪ" << i;
    std::cout << ",����countΪ" << count << std::endl;
}