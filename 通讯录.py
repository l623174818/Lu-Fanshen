'''
    Author:Lu Fanshen
    Function:Homework
    Version:1
    Date:
    Comments:
'''

menu = 0
lxr = {}
while(menu != 4):
    print('''
    菜单
    [1]	新增联系人
    [2]	删除联系人
    [3]	联系人列表
    [4]	退出
    ''')
    menu = input('请输入功能：')
    if menu.strip():
        menu = int(menu)
        if menu == 1:
            print('''
            新增联系人
            按两次[回车键]返回主层菜单
            ''')
            name = input('姓名:')
            value = lxr.__contains__(name)
            if value == True:
                print('联系人已存在')
            else:
                number = input('联系电话:')
                if number.strip():
                    lxr[name] = number
                    print('联系人已保存')
                else:
                    print('已返回主菜单')
        if menu == 2:
            print('''
            删除联系人
            按[回车键]返回主层菜单
            ''')
            name = input('姓名:')
            value = lxr.__contains__(name)
            if name.strip():
                if value == True:
                    del lxr[name]
                    print('联系人已删除')
                else:
                    print('联系人不存在')
        if menu == 3:
            print('联系人列表')
            print(lxr)
            print(len(lxr),'位联系人')
        
print('再见！')
