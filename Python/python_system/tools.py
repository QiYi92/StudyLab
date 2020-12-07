info_list = []


def show_menu():
    """显示菜单"""
    print('-' * 50)
    print('欢迎使用员工系统')
    print('')
    print('1.新建员工')
    print('2.显示全部')
    print('3.查找员工')
    print('')
    print('0.退出系统')
    print('-' * 50)


def new_employee():
    """新建员工"""
    print('-' * 50)
    print('功能：新增员工')

    # 提示用户输入员工信息
    name = input('请输入姓名:')
    phone = input('请输入电话:')
    qq = input('请输入qq:')
    email = input('请输入邮箱地址:')

    # 保存到字典
    info_dict = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }

    info_list.append(info_dict)

    print("成功添加员工:{}".format(info_dict["name"]))


def show_all():
    """显示全部"""
    print('-' * 50)
    print('功能：显示全部')

    if len(info_list) == 0:
        print('提示：没有任何名片记录')

        return

    for name in ['姓名', '电话', 'QQ', '邮箱']:
        print(name, end='\t\t')

    print('')
    print('='*50)
    for employee_info in info_list:
        print('{}\t\t{}\t\t{}\t\t{}' .format(employee_info['name'],
                                             employee_info['phone'],
                                             employee_info['qq'],
                                             employee_info['email'],)),


def search_employee():
    """查找员工"""
    print('-'*50)
    print('功能：查找员工')

    # 根据要搜索的姓名
    find_name = input('请输入要搜索的姓名:')

    # 遍历
    for employee_dict in info_list:
        if employee_dict['name'] == find_name:

            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print('-'*50)

            print('{}\t\t\t{}\t\t\t{}\t\t\t{}'.format(employee_dict['name'],
                                                      employee_dict['phone'],
                                                      employee_dict['qq'],
                                                      employee_dict['email'],))
            print('-'*50)

            break
        else:
            print("没有找到{}".format(find_name))

def deal_employee(find_dict):
    """操作搜索到的员工字典"""
    print(find_dict)

    action_str = input('请选择要操作的序号:'
                       '[1] 修改 [2]删除 [0]返回主菜单')

    if action_str == '1':
        print("修改")

        find_dict['name'] = input("输入姓名")
        find_dict['phone'] = input("输入电话")
        find_dict['qq'] = input("输入QQ")
        find_dict['email'] = input("输入邮件")

        print("{}的名片修改成功".format(find_dict["name"]))

    elif action_str == '2':
        print("删除")
        info_list.remove(find_dict)
        print("删除成功")

def input_employee_info(dict_value,tip_message):
    """输入名片信息"""
    res_str = input(tip_message)
