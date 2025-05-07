#大漠只能被32位的python调用，操作系统不用换，64位的操作系统也能安装32位的python


#你的python中需要安装pypiwin32模块，安装命令如下：

#pip install pypiwin32 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com


#在本地电脑系统中注册大漠：


#如果你是64位操作系统，需要把dm.dll复制到c:\windows\syswow64

#这个文件夹中

#管理员权限打开cmd，转到syswow64目录下，运行regsvr32 dm.dll，注册成功


#注册过程中如果出现错误，则可能是你之前注册过，
#regsvr32 dm.dll /u
#这个命令可以进行卸载，然后再次尝试

# 注册

#python调用大漠示例代码：


import win32com.client
import random
import time
dm=win32com.client.Dispatch('dm.dmsoft')#调用大漠插件，获取大漠对象

print(dm.ver())#输出大漠版本号
# 333144

dm.SetPath(r'E:\\python_work_speace\\test\\003点击操作')
st = time.time()
# hwnd = dm.GetMousePointWindow()
hwnd = 1120232
print('hwnd = ',hwnd)
print('hwn type is = ',type(hwnd))
# dm_ret = dm.BindWindowEx(hwnd,"dx","normal","normal","",0)
dm_ret = dm.BindWindowEx(hwnd,"gdi","windows","windows","",0)
# dm_ret = dm.BindWindowEx(hwnd,"gdi2","windows","windows","",0)
# dm_ret = dm.BindWindowEx(hwnd,"gdi","windows","windows","",0)
pic_name = str(random.randint(0,1000000))+"screen.bmp"
print('this is pic_name: ',pic_name)
# dm_ret = dm.Capture(0,0,2000,2000,pic_name)
intX,intY = 0,0
dm_ret = dm.FindPic(0,0,540,960,r"E:\python_work_speace\test\003点击操作\wangzhe.bmp","000000",0.9,0,intX,intY)
print('dm find result :dm_ret = ',dm_ret)
if intX >= 0 and intY >= 0:
    print(f'find pic intX = {intX}, intY = {intY}')
    print(f'find pic intX = {dm_ret[1]}, intY = {dm_ret[2]}')
    dm_ret = dm.MoveTo(dm_ret[1],dm_ret[2])
    dm_ret = dm.LeftClick()
dm_ret = dm.UnBindWindow()
print("本次操作耗时：", time.time() - st)

'''
dm_ret = dm.BindWindowEx(hwnd,"normal","normal","normal","",0)
'''