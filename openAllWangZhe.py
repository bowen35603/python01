import win32com.client
import random
import time
st = time.time()
dm=win32com.client.Dispatch('dm.dmsoft')#调用大漠插件，获取大漠对象

print(dm.ver())#输出大漠版本号
# 333144
'''
parent 整形数: 获得的窗口句柄是该窗口的子窗口的窗口句柄,取0时为获得桌面句柄

title 字符串: 窗口标题. 此参数是模糊匹配.

class_name 字符串: 窗口类名. 此参数是模糊匹配.

filter整形数: 取值定义如下

1 : 匹配窗口标题,参数title有效 

2 : 匹配窗口类名,参数class_name有效.

4 : 只匹配指定父窗口的第一层孩子窗口

8 : 匹配所有者窗口为0的窗口,即顶级窗口

16 : 匹配可见的窗口

32 : 匹配出的窗口按照窗口打开顺序依次排列 <收费功能，具体详情点击查看>

这些值可以相加,比如4+8+16就是类似于任务管理器中的窗口列表
'''

hwnds = dm.EnumWindow(0,"","RenderWindow",2+16)
print('hwnds = ',hwnds)
# hwnds = split(hwnds,",")
leidians = hwnds.split(",")
# 查找到所有的雷电窗口句柄

print('leidians = ',leidians)
print("截图耗时：", time.time() - st)
# hwnds = split(hwnds,",")

def click(hwnd):
    print("click hwnd : ",hwnd) 
    dm2=win32com.client.Dispatch('dm.dmsoft')#调用大漠插件，获取大漠对象
    dm_ret = dm2.BindWindowEx(hwnd,"gdi","windows","windows","",0)
    print("绑定雷电窗口 : ",dm_ret)   # 绑定雷电窗口
    dm_ret = dm2.FindPic(0,0,2000,2000,r"E:\python_work_speace\test\003点击操作\003.bmp","202020",0.6,0,0,0)
    print("查找图片 : ",dm_ret)   # 查找图片
    dm_ret = dm2.MoveTo(dm_ret[1],dm_ret[2])
    dm_ret = dm2.LeftClick()
    print("leftclick : ",dm_ret)   #  点击结果
    
    dm_ret = dm2.UnBindWindow()


# 依次操作雷电窗口
for leidian in leidians:
    print("leidian = ",leidian)
    st = time.time()
    click(leidian)
    print("leidian  click耗时：", time.time() - st)
    # time.sleep(0.4)
    print("**"*30)

    
# dm_ret = dm.BindWindow(leidian,"","RenderWindow",1,0,0,0)
'''
    leidian =  1120232
    leidian =  1248774
    leidian =  2692254
    
    long FindWindowEx(parent,class,title) 

    参数定义:

    parent 整形数: 父窗口句柄，如果为空，则匹配所有顶层窗口

    class 字符串: 窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.

    title 字符串: 窗口标题,如果为空，则匹配所有. 这里的匹配是模糊匹配.

    pyinstaller --onefile openAllWangZhe.py


'''
    