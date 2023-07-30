import os
file = '学生信息储存.txt'

#主程序
def main():
    while True:
        menu()
        select = int(input('请输入\n'))
        if select in [0,1,2,3,4,5,6,7]:
            if select == 1:
                insert()
            elif select == 2:
                search()
            elif select == 3:
                delete()
            elif select == 4:
                modify()
            elif select == 5:
                sort()
            elif select == 6:
                total()
            elif select == 7:
                show()
            elif select == 0:
                answer = input('确定退出吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！')
                    break
                else:
                    continue

#菜单
def menu():
    print('''===============学生信息管理系统===============

------------------功能菜单-------------------
            1.录入学生信息
            2.查找学生信息
            3.删除学生信息
            4.修改学生信息
            5.排序
            6.统计学生总人数
            7.显示所有学生信息
            0.退出系统


--------------------------------------------''')

#信息列表
def list(lst):
    i = lst
    print('id\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总成绩')
    print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}'.format(i.get('id'),i.get('name'),str(i.get('Chinese')),str(i.get('Math')),str(i.get('English')),str(int(i.get('Chinese')+int(i.get('Math'))+int(i.get('English'))))))

#信息录入模块
def insert():#信息录入系统
    d_lst = []
    while True:
        try:
            id = input('输入id序号（如1001）：')
            name = input('输入学生姓名：')
            Chinese = int(input('语文成绩：'))
            Math = int(input('数学成绩：'))
            English = int(input('英语成绩：'))
        except:
            print('输入错误,成绩请输入整数！')
        else:
            d_lst.append({'id':id ,'name':name ,'Chinese':Chinese ,'Math':Math ,'English':English})
        select = str(input('是否继续录入？y/n'))
        if select == 'y' or select == 'Y':
            continue
        else:
            if d_lst:
                save(d_lst)
            return
    if d_lst:
        save(d_lst)

#保存模块
def save(lst):
    lst1 = []
    if not lst:
        print('程序错误,列表为空')
    else:
        txt = open(file,'a',encoding='utf-8')
        for i in lst:
            lst1.append(i)
            txt.write(str(lst1)+'\n')
            lst1 = []
        txt.close()

#显示模块
def show():
    i_lst = []
    if os.path.exists(file):
        txt = open(file,'r',encoding='utf-8')
        d = txt.readlines()
        if d:
            print('id\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总成绩')
            for a in d:
                for i in eval(a):
                    i_lst.append(eval(str(i)))
            stu_show(i_lst)
            txt.close()
        else:
            print('尚未录入数据！')
    else:
        print('尚未录入数据！')

#小遍历模块
def stu_show(lst):
    for i in lst:
        print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}'.format(i.get('id'),i.get('name'),str(i.get('Chinese')),str(i.get('Math')),str(i.get('English')),str(int(i.get('Chinese')+int(i.get('Math'))+int(i.get('English'))))))

#搜索模块
def search():
    lst = []
    while True:
        with open(file,'r',encoding='utf-8') as txt:
            d = txt.readlines()
            if not d:
                print('尚未录入信息')
                break
            for o in d:
                o = eval(o)
                for i in o:
                    lst.append(i)
        select = input('id查询请扣1，姓名查询请扣2')
        sear = 0
        if select == '1':
            id_search = input('请输入要查询的id：')
            for i in lst:
                if i.get('id') == id_search:
                    print('已查询到id：'+id_search)
                    list(i)
                    sear = 1
        elif select == '2':
            name_search = input('请输入要查询的姓名：')
            for i in lst:
                if i.get('name') == name_search:
                    print('已查询到姓名：'+name_search)
                    list(i)
                    sear = 1
        else:
            print('自动返回主界面')
            break
        if sear == 0:
            print('查无此人')
        choice = input('是否继续查询？y/n')
        if choice == ('y' or 'Y'):
            continue
        else:
            break

#删除模块
def delete():
    lst = []
    lst1 = []
    lst2 = []
    while True:
        with open(file, 'r', encoding='utf-8') as txt:
            d = txt.readlines()
            if not d:
                print('尚未录入信息')
                break
            for o in d:
                o = eval(o)
                for i in o:
                    lst.append(i)
        select = input('id删除请扣1，姓名删除请扣2')
        if select == '1':
            id_search = input('请输入要删除的id：')
            for i in lst:
                if i.get('id') != id_search:
                    lst1.append(i)
                else:
                    print('已删除')
            if lst1 == lst:
                print('未查询到该id')
        elif select == '2':
            name_search = input('请输删除的姓名：')
            for i in lst:
                if i.get('name') != name_search:
                    lst1.append(i)
                else:
                    print('已删除')
            if lst1 == lst:
                print('未查询到该姓名')
        else:
            print('自动返回主界面')
            break
        txt = open(file,'w',encoding='utf-8')
        for i in lst1:
            lst2.append(i)
            txt.write(str(lst2)+'\n')
            lst2 = []
        txt.close()
        choice = input('是否继续删除？y/n')
        if choice == ('y' or 'Y'):
            continue
        else:
            break

#排序模块
def sort():
    if os.path.exists(file):
        txt = open(file,'r',encoding='utf-8')
        d = txt.readlines()
        txt.close()
        if not d:
            print('尚未录入信息')
        else:
            if d:
                stu = []
                for i in d:
                    for a in eval(str(i)):
                        stu.append(a)
                show()
                select = input('''1.按id排序
2.按语文成绩排序
3.按数学成绩排序
4.按英语成绩排序
5.按总成绩排序
请输入：''')
                mode = int(input('''0.升序
1.降序
请输入：'''))
                if mode in [0,1]:
                    if select == '1':
                        stu.sort(key=lambda stu : int(stu['id']),reverse=bool(mode))
                        stu_show(stu)
                    elif select == '2':
                        stu.sort(key=lambda stu: int(stu['Chinese']), reverse=bool(mode))
                        stu_show(stu)
                    elif select == '3':
                        stu.sort(key=lambda stu: int(stu['Math']), reverse=bool(mode))
                        stu_show(stu)
                    elif select == '4':
                        stu.sort(key=lambda stu: int(stu['English']), reverse=bool(mode))
                        stu_show(stu)
                    elif select == '5':
                        stu.sort(key=lambda stu: int(stu['Chinese'])+int(stu['Math'])+int(stu['English']), reverse=bool(mode))
                        stu_show(stu)
                    else:
                        print('自动返回菜单')
                else:
                    print('自动返回菜单')
            else:
                print('尚未录入成绩')
    else:
        print('尚未录入成绩')

#修改模块
def modify():
    lst = []
    while True:
        with open(file, 'r', encoding='utf-8') as txt:
            d = txt.readlines()
            if not d:
                print('尚未录入信息')
                break
            for o in d:
                o = eval(o)
                for i in o:
                    lst.append(i)
        sear = 0
        select = input('id查询请扣1，姓名查询请扣2')
        if select == '1':
            id_search = input('请输入要查询的id：')
            for i in lst:
                if i.get('id') == id_search:
                    print('已查询到id：' + id_search)
                    list(i)
                    sear = 1
        elif select == '2':
            name_search = input('请输入要查询的姓名：')
            for i in lst:
                if i.get('name') == name_search:
                    print('已查询到姓名：' + name_search)
                    list(i)
                    sear = 1
        else:
            print('自动返回主界面')
            break
        if sear == 1:
            try:
                id = input('输入id序号（如1001）：')
                name = input('输入学生姓名：')
                Chinese = int(input('语文成绩：'))
                Math = int(input('数学成绩：'))
                English = int(input('英语成绩：'))
            except:
                print('输入错误，修改失败，成绩请输入整数！')
            else:
                txt = open(file,'w',encoding='utf-8')
                d_dic = {'id': id, 'name': name, 'Chinese': Chinese, 'Math': Math, 'English': English}
                lst1 = []
                lst2 = []
                if select == '1':
                    for i in lst:
                        if i.get('id') != id_search:
                            lst1.append(i)
                        else:
                            lst1.append(d_dic)
                    for i in lst1:
                        lst2.append(i)
                        txt.write(str(lst2) + '\n')
                        lst2 = []
                elif select == '2':
                    for i in lst:
                        if i.get('name') != name_search:
                            lst1.append(i)
                        else:
                            lst1.append(d_dic)
                    for i in lst1:
                        lst2.append(i)
                        txt.write(str(lst2) + '\n')
                        lst2 = []
                txt.close()
        choice = input('是否继续修改？y/n')
        if choice == ('y' or 'Y'):
            continue
        else:
            break

#统计模块:
def total():
    if os.path(file):
        txt = open(file,'r',encoding='utf_8')
        d = txt.readlines()
        if d:
            print('共计'+str(len(d))+'人')
            txt.close()
        else:
            print('尚未录入信息')
    else:
        print('尚未录入信息')
#程序，启动！
if __name__ == '__main__' :
    main()