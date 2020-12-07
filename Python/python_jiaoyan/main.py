# --coding:utf-8--
W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 加权系数
M_run = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 闰年每月天数
M_ping = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年每月天数

while True:
    while True:
        id_number = input('请输入一个18位的身份证号码：')
        if len(id_number) != 18 or not id_number[:-1].isdigit() or not \
                id_number[-1].isdigit() and (id_number[-1] != 'X' or id_number[-1] != 'x'):
            print('身份证号码错误')
        else:
            break
    while True:
        id_sex = input('请输入性别：')
        if id_sex != '男' and id_sex != '女':
            print('性别错误')
        else:
            break
    print('身份证号：', id_number)
    print('性    别：', id_sex)
    id_number_dict = dict()
    id_number_dict['地址码'] = int(id_number[:6])
    # 校验身份证地址码
    if len(str(id_number_dict['地址码'])) != 6:
        print('身份证号码地址码错误')
        continue
    id_number_dict['YY'] = int(id_number[6:10])
    # 校验身份证年份
    if len(str(id_number_dict['YY'])) != 4 or id_number_dict['YY'] > 2019:
        print('身份证号码年份错误')
        continue
    id_number_dict['MM'] = int(id_number[10:12])
    # 校验身份证月份
    if id_number_dict['MM'] > 12 or id_number_dict['MM'] == 0:
        print('身份证号码月份错误')
        continue
    id_number_dict['DD'] = int(id_number[12:14])
    # 校验身份证日期
    if id_number_dict['YY'] % 400 == 0 or (id_number_dict['YY'] % 4 == 0 and id_number_dict['YY'] % 100 != 0):
        if id_number_dict['DD'] > M_run[id_number_dict['MM']-1]:
            print('身份证号码日期错误')
            continue
    else:
        if id_number_dict['DD'] > M_ping[id_number_dict['MM']-1]:
            print('身份证号码日期错误')
            continue
    id_number_dict['顺序码'] = id_number[14:17]
    # 校验身份证顺序码
    if (int(id_number_dict['顺序码'][-1]) % 2 == 0 and id_sex == '男') or (
            int(id_number_dict['顺序码'][-1]) % 2 == 1 and id_sex == '女'):
        print('身份证号码顺序码错误')
        continue
    if id_number[17] == 'X' or id_number[17] == 'x':
        id_number_dict['校验码'] = 10
    else:
        id_number_dict['校验码'] = int(id_number[17])
    # 校验身份证校验码
    A = list(map(int, list(id_number[:-1])))
    id_S = sum([x * y for (x, y) in zip(A, W)])
    id_N = (12 - id_S % 11) % 11
    if id_N == id_number_dict['校验码']:
        print('身份证合法')
    else:
        print('身份证不合法')
    is_continue = input('是否继续校验身份证号码，请输入（y/n）：')
    if is_continue == 'n':
        print('结束')
        break
