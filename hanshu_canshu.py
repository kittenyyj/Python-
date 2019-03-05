def stu(name,age,*args,hobby="没有",**kwargs):
    '''
    :param name:
    :param age:
    :param args:
    :param hobby:
    :param kwargs:
    :return:
    '''
    print("大家好")
    print("我叫{0}，我今年{1}岁了".format(name,age))
    if hobby=="没有":
        print("我没有爱好")
    else:
        print("我的爱好是{0}".format(hobby))
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,"  ",v)
#正常调用
name="yyj"
age=23
stu(name,age,"看电视","玩游戏",hobby="听歌",hobby2="看书",hobby3="写代码")
print("*"*30)
#解包
l=["看电视","玩游戏"]
t={'hobby2':"看书",'hobby3':"写代码"}
stu(name,age,*l,hobby="听歌",**t)