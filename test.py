from pygameauto import *


obj = Obj()
res = obj.register(r"E:\\python_work_speace\\test\DmReg.dll", 
             r"E:\\python_work_speace\\test\\dm.dll")
print("注册结果是：" , res)

res = obj.create()

print("创建结果是： " , res)

print("大漠版本号: ",obj.Ver())

# obj = Obj()
# obj.register(r".\DmReg.dll", r".\dm.dll")
# obj.create()