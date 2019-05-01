#学生类
class Student:
    def __init__(self,stuId,name,age):
        self.stuId = stuId
        self.name = name
        self.age = age

    # def studentoop(self):
    #     pass

#全局变量
new_stuId = ""
new_name = ""
new_age = ""

#管理系统类
class Sys:
    def __init__(self):
        pass

    #展示系统菜单
    def show_menu(self):
        print("=" *66)
        print("                  学生管理系统")
        print("                 1:添加学生信息")
        print("                 2:查询学生信息")
        print("                 3:修改学生信息")
        print("                 4:删除学生信息")
        print("                 5:显示学生信息")
        print("                 6:退出系统")
        print("=" * 66)

    #输入学生菜单
    def getinfo(self):
        global new_stuId
        global new_name
        global new_age
        new_stuId = input("请输入学号：")
        new_name = input("请输入名字：")
        new_age = input("请输入年龄：")

    #添加学生信息
    def add_stus(self):
        #调用getinfo方法
        self.getinfo()
        # 以ID为Key,将新输入的信息赋值给Student类
        students[new_stuId] = Student(new_stuId,new_name,new_age)

        # 打印添加的学生信息
        print("ID:%s"%students[new_stuId].stuId,"Name:%s"%students[new_stuId].name,"Age:%s"%students[new_stuId].age)

    def find_stus(self):
        find_nameId = input("请输入要查的学号：")
        if find_nameId in students.keys():
            print("学号：%s\t名字：%s\t年龄：%s"%(students[new_stuId].stuId, students[new_stuId].name, students[new_stuId].age))
        else:
            print("查无此人")

    def alter_stus(self):
        alterId = input("请输入你要修改的学生的学号：")
        self.getinfo()
        # 当字典中Key相同时，覆盖掉以前的key值
        if alterId in students.keys():
            students[new_stuId] = Student(new_stuId,new_name,new_age)
            del students[alterId]
        else:
            print("查无此人")

    # 删除学生信息
    def del_stus(self):
        cut_nameID = input("请输入要删除的学号：")
        if cut_nameID in students.keys():
            del students[cut_nameID]
        else:
            print("查无此人")

    # 显示学生信息
    def show_stus(self):
        for new_stuId in students:
            print("ID:%s" % students[new_stuId].stuId, "Name:%s" % students[new_stuId].name,"Age:%s" % students[new_stuId].age)

    #退出系统
    def exit_stus(self):
        print("欢迎下次使用")
        exit()

# 创建系统对象
sys = Sys()
# 定义一个容器来存储学生信息
students = {}
while True:
    sys.show_menu()
    choice = int(input("请选择你需要的功能，输入相应数字："))
    if choice == 1:
        sys.add_stus()
    elif choice == 2:
        sys.find_stus()
    elif choice == 3:
        sys.alter_stus()
    elif choice == 4:
        sys.del_stus()
    elif choice == 5:
        sys.show_stus()
    elif choice == 6:
        sys.exit_stus()
    else:
        print("！！！输入有误，请重新确认，输入正常数字")