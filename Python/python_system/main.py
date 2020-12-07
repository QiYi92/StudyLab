import tools

while True:

    tools.show_menu()

    action = input('请选择操作功能：')
    print('你选择的功能序号是：{}'.format(action))
    if action in ['1', '2', '3']:
        if action == '1':
            tools.new_employee()

        elif action == '2':
            tools.show_all()

        elif action == '3':
            tools.search_employee()

    elif action == '0':
        print('欢迎再次使用')
        break

    else:
        print('你的输入有误')
