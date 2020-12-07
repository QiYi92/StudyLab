#include <iostream>
#include <conio.h>
#include <string>
using namespace std;

class student
{
    private:
        long xh; //学生编号
        char mz[10]; //学生名字
        char xb[2]; //学生性别
        char zy[40]; //专业名称
        char bj[10]; //班级名称
        char nj[10]; //年级名称
        char dz[40]; //家庭住址
        long dh; //电话号码
    public:
        void cinnumber()
        {
            cout << "请输入学生编号";
            cin >> xh;
            cout << endl;

            cout << "请输入学生名字";
            cin >> mz;
            cout << endl;

            cout << "请输入学生性别";
            cin >> xb;
            cout << endl;

            cout << "请输入专业名称";
            cin >> zy;
            cout << endl;

            cout << "请输入班级";
            cin >> bj;
            cout << endl;

            cout << "请输入年级";
            cin >> nj;
            cout << endl;

            cout << "请输入家庭住址";
            cin >> dz;
            cout << endl;

            cout << "请输入电话号码";
            cin >> dh;
            cout << endl;
        }

        void coutnumber()
        {
            cout << "学生信息：" << endl;
            cout << "学生编号:" << xh <<endl;
            cout << "学生名字:" << mz <<endl;
            cout << "学生性别:" << xb <<endl;
            cout << "专业名称:" << zy <<endl;
            cout << "班级:" << bj <<endl;
            cout << "年级:" << nj <<endl;
            cout << "家庭住址" << dz << endl;
            cout << "电话号码" << dh << endl;
        }
};

int main()
{
    student s1;
    s1.cinnumber();
    s1.coutnumber();
    return 0;
}
