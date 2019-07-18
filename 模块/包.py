
#把解决一类问题的模块放在用一个文件夹里----包


'''(1)import packtest.db.dbtest
  packtest.db.dbtest.dbfunc()
#从packtest包中的db包中导入dbtest这个模块

(2)from packtest.db import dbtest（from...import 后面必须是一个明确的，不能带点的
）
    packtest.db.dbtest.dbfunc()


(3)添加导入模块的路径
    import sys
    sys.path.insert(0,'/Users/suyayan/PycharmProjects/helloworld/模块/packtest/api')
    import apitest
    apitest.apifunc()

（4）import packtest
     import一个包，不能执行这个包内子文件内的模块，只能执行这个包内的模块




'''
import packtest
packtest.api.apitest.apifunc()