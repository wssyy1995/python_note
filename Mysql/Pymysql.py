#验证登录用户密码是否正确
'''

import pymysql
username=input('login username:')
password=input('password:')


#连接mysql
mscon=pymysql.connect(host='localhost',user='root',password='wxxxx,yyqxxxx8',database='yayandb1')

cursor=mscon.cursor()


#cursor执行，返回执行结果
# sql="select * from account where username='%s' and password='%s';"%(username,password)
# cursor.execute(sql)


sql="select * from account where username=%s and password=%s;"
cursor.execute(sql,[username,password])


#通过fetch来从执行结果中拿一个
result=cursor.fetchone()
print(result)


#关闭连接
cursor.close()
mscon.close()

if result:
    print('log in successful')
else:print('log in fail ,please check you username and password')




#sql注入问题：
    #sql="select * from account where username='%s' and password='%s';"%(username,password)
    #借用了python注释的原理，通过输入'来跳过验证  ：yayan ' or 1=1#

#解决方式：写sql语句是，不要写字符串拼接，execute会自动执行字符串拼接
    # sql="select * from account where username=%s and password=%s;"
    # cursor.execute(sql,[username,password])

'''


#pymysql增删改查：
import pymysql
mscon=pymysql.connect(host='localhost',user='root',password='wssyy,yyqx1128',database='yayandb1')
cursor=mscon.cursor()

#增加
#将添加某个用户的代码封装成方法
def addauser():
    username = input('please input your signup username:')
    password = input('please input your signup password:')
    sql = "insert into account(username,password) values(%s,%s)"
    cursor.execute(sql, [username, password])

    # 如果进行增删改，必须进行commit,select不需要
    mscon.commit()

    cursor.close()
    mscon.close()


#删除：
#将删除某个用户的代码封装成方法
def delauser():
    username=input('please input your delete username:')
    password=input('please input your delete passwword:')
    sql="delete from account where username=%s and password=%s "
    cursor.execute(sql,[username,password])

    #删完之后需要重新对id排序
    改
    def idreorder():
        sqldid="alter table account drop id;"
        sqlaid="alter table account add column id int not null auto_increment primary key first"
        cursor.execute(sqldid)
        cursor.execute(sqlaid)
    idreorder()

    #如果进行增删改，必须进行commit,select不需要
    mscon.commit()

    cursor.close()
    mscon.close()


#查

sql="select * from account;"
cursor.execute(sql)

#fetchone()拿一条结果,默认第一条数据
result=cursor.fetchone()
print(result)

#fetchmany(4)拿几条数据
result=cursor.fetchmany(3)
print(result)

#fetchall()拿全部数据sql="select * from account;"
result=cursor.fetchall()
print(result)









cursor.close()
mscon.close()

