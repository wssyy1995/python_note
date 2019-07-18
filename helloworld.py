'''count=1
sum=0
while count <= 100:
    sum = sum + count
    count=count+1

print(sum)
'''
#input
'''name = input("what's your name ? ")
age = input("how old are you ?")
print("your age is:"+age+",""your name is :"+name)
'''

#while
'''count=1
while True:
    print(count)
    count=count + 1
    if count > 100:
        break
'''

#continue
'''count=0
while count <= 100 :
    count += 1
    if count > 5 and count < 95 :
        continue
    print(count)
'''
'''a=1
b=1
count = 5
if count > 8 :
    a=3
b=3
print(a,b)'''

'''count=0
while count <= 100 :
    count += 1
    if count <= 5 or count >= 95 :
        print(count)'''

#用while输出1234568910
'''count = 0
while count < 10:
    count += 1
    if count == 7 :
        print(' ')
        continue
    print(count)'''





#3次登录机会
"""i = 0
rname = 'suyayan'
rpw = '092628'
while i < 3 :
    iname= input("please input the account name :")
    ipw = input("Please input the password:")
    if iname == rname and ipw == rpw :
        print("login successfully")
        break
    else:
        print("login failed,you now have %d chances" %(2-i))
        if (2-i) == 0 :
            result = input('do you want try again?Yes')
            if result == 'Yes':
                i = 0
                continue

    i += 1
else: print("buyaolian")
"""


#格式化输出

"""
name = input("please input your name :")
age = input("please input your age :")
job = input("please input your job :")
hobbie = input("please input your hobbie :")
print('''------------info of %s------
Name : %s
Age : %d 
Job : %s
Hobbie : %s''' %(name,name,int(age),job,hobbie))
"""
#三元运算：
#a = 条件返回True的结果 if 条件 else 条件返回False的结果

#print( 3>1 or 2 and 3>5)

'''count =0
sum=0
while count < 99 :
    count += 1
    if count == 88: continue
    if count%2 == 1 :
        sum = sum + count
    else : sum = sum - count

print(sum)
'''
'''count = 0
j = -1
sum = 0
while count < 99 :
    count += 1
    if count == 88 :continue
    j = -j
    sum = sum + count*j

print(sum)
'''

'''s='ABCDEF'
s1=s[0:5:2]
print(s1)'''

'''s='guangjSB'
s1 = s.capitalize()
print(s1)'''

'''s='guangJJSD in is a sb'
s2=s.title()
print(s2)
'''

'''print('what is your name?')
name = input('my name is :')
if name.startswith('guang') == True :
    print('you are sb!')
else: print('you are cute!')
'''

'''print('what is your name?')
name = input('my name is :')
sbname = name[0:5]
print(sbname)
if sbname == 'guang':
    print('you are sb!')
else: print('you are cute!')
'''

'''s='guangjing is a sb'
s1=s.index('sb',0,5)
print(s1)
'''

'''name= input()
name2=name.strip()
if name2 == 'guangjing' :
    print('you are sb')
else : print ('i am sb')
'''

'''name= 'a  abcd12344444444444444444444'
name2 = name.strip('a4')
print(name2)
'''
'''name = 'abcabcabcabdddeeeffff'
s=name.count('ff')
print(s)
'''

'''s='guang yayan suisui'
s2=s.split()
print(s2,type(s2))
'''

'''name = input('what is your name :')
age = int(input('how old are you?'))
hobbie = input('what is your hobbie?')

s = 'my name is : %s , my age is %d,my hobbie is %s'%('sb',age,hobbie)

s1 = 'my name is : {} , my age is {},my hobbie is {}'.format(name,age,hobbie)

s2= 'my name is : {2} , my age is {1},my hobbie is {0}'.format(hobbie,age,'sb')

s3='my name is : {a} , my age is {b},my hobbie is {c}'.format(a =name,b = age,c='eating')

print(s+'\n'+s1+'\n'+s2+'\n'+s3)

name=input('sdfjfdsdf sldjf: ')
if 'guangjing' in name:
    print('he is sb')
'''

'''s='132a4b5c'
s2=s[0]+s[2:0:-1]
print(s2)'''

'''s='c  abc  '
s2=s.split()
print(s2)
'''
'''l=['guangjing','yayan','suisui',[1,2,'abc']]
print(l)
l2=l.append(['sb',4,5,6])
print(l2)'''

'''l=['guangjing','yayan','suisui',[1,2,'abc']]
#l.insert(1,'this is sb')
#l.extend([1,2,3,'sb','bs'])
#l2=l.pop(2)
#l[0:]='papa'
#l1=l.index([1,2,'abc'])
#l1=[1,2,3,5,4,7,6]
#l1=l[3][2]
#l[0]=l[0].capitalize()
#l[3][2]=l[3][2].upper()
print(l)'''

'''l=('guangjing','yayan','suisui','papa')
#l[2][1]='suisuisb'
l2='sb'.join(l)
print(l2) '''


'''s='guang'
s1='sb'.join(s)
print(s1)
'''

'''for i in range(8):
    print(i)
    '''

'''dic = {'name':['guangjing','yayan'],'age':[17,18],'pet':{'petname':'suisui','petage':'6month'}}
print(dic.get('age'))
'''

'''for k in dic.values():
    print(k)
    '''

#dic['pet']['petsex']='female'
#print(dic)
#dic['name'][0]= dic['name'][0].replace('guang','sb')
'''print(dic.items())
for k,v in dic.items():
    print(k,v)
print(dic.get('hobbie','no this key'))
'''
'''print(dic.keys())
print(dic.values())
print(dic.items())
for i in dic.items ():
    print(i)
    '''
'''dic['hobbie']=['write bug','test bug']
#dic.pop('sb','there are none')
dic2={'age':[17,18],'animal':['pig','dog']}
dic.update(dic2)
print(dic)
'''

'''l=('gu','su',['jing','yayan'],(1,2,3,['a','b']))
#l[2][0]='ji'
l[3][3].append(5)
print(l)
'''
'''l1=[]
l2=[]
dic={'k1':l1,'k2':l2}
li = [11,22,33,44,55,66,77,88,99,90]
for i in li:
    if i== 66 :continue
    elif i >66:
        l1.append(i)
    else:l2.append(i)
print(dic)
'''

'''s='光景guangjing'
s1=s.encode('utf-8') # s是默认unicode编码的str，将转换为utf-8编码的bytes类型
print(s,'\n',s1)
'''

#li=[{'apple':10},{'banana':20},{'lemon':30}]
'''li=[{'商品':'苹果','价格':10},{'商品':'香蕉','价格':20},{'商品':'西瓜','价格':30}]
print('欢迎来到sb水果商店')
money = input('你有多少钱:')
if money.strip().isdigit() and int(money)>0:
    while 1 :
        for i, k in enumerate(li):
            print('序号:{}    商品名字:{}    价格:{}'.format(i + 1, k['商品'], k['价格']))
        choose=input('请输入你要购买的商品序号:')
        if choose.isdigit() and int(choose)<= len(li):
            num=input('你想要购买多少 ?请输入数量：')
            if num.isdigit() and int(num)>0:
                total=int(num)*li[int(choose)-1]['价格']
                item=li[int(choose)-1]['商品']
                balance=int(money)-int(num)*li[int(choose)-1]['价格']
                if int(money)< total:
                    print('金额不足，总计需要:{},你的余额为:{}'.format(total,int(money)))
                else:
                    confirm = input('你即将购买{}个{},总计花费{}元，你确定吗？'.format(int(num),item,total))
                    if confirm.strip().upper()=='YES':
                        print('购买成功，你的余额为{}'.format(balance))
            else:print('你输入的不是数字或者输入数量为0')
        else:print('你输入的序号有误')

else:print("你输入的金额不正确或者少于0")
'''

'''set1={1,2,3,'abc'}
print(set1)
set2=frozenset(set1)
print(set2)
set1.remove(1)
print(set1)
set2.remove(1)
print(set2)
#set2.add(4)
#print(set2)'''

'''lis=[1,2,3,4,5]
for i in range(len(lis)):
    print(i)
    print(lis)
    del lis[i]
    '''

'''lis=[1,2,3,4,5]
for i in range(len(lis)):
    print(i)
    i=i-i
    del lis[i]
    print(lis)
    '''


'''dic={'name':'sb','age':18}
del dic['name']
print(dic)
'''
#绝对路径
'''guangjing=open('/Users/suyayan/Downloads/py file operation/guangjingsb.text',mode='r',encoding='utf-8')
content = guangjing.read()
print(content)
guangjing.close
'''
#相对路径
'''sui = open('suisui.text',mode='r',encoding='utf-8')
content = sui.read()
print(content)
'''

#mode

'''sui = open('suisui.text',mode='rb')
content = sui.read()
print(content)
'''

'''niuyouguo = open('/Users/suyayan/Library/Mobile Documents/com~apple~CloudDocs/绿色我爱学习/牛油果每日日程压缩.pdf',mode='r'，encoding='utf-8')
content = niuyouguo.read()
print(content,'\n',type(content))

hello = open('/Users/suyayan/Downloads/py file operation/writetest.text',mode='w',encoding='utf-8')
hello.write('this is a writetest content')
hello.close()

readhello = open('/Users/suyayan/Downloads/py file operation/writetest.text',mode='r',encoding='utf-8')
content=readhello.read()
print(content)
'''

'''hello2=open('/Users/suyayan/Downloads/py file operation/writetest2.text',mode='wb')
hello2.write( 'this is a wb write test'.encode('utf-8'))
hello2.close()

zhuijia =open('/Users/suyayan/Downloads/py file operation/writetest2.text',mode='a',encoding='utf-8')
zhuijia.write('this is a zuijia content ')
zhuijia.close()
'''

'''rwtest = open('/Users/suyayan/Downloads/py file operation/writetest.text',mode='r+',encoding='utf-8')
rwtest.write('read and write')
r=rwtest.read()
print(r)
'''

'''wrtest = open('/Users/suyayan/Downloads/py file operation/writetest.text',mode='w+',encoding='utf-8')
wrtest.write('mingbai  ')
print(wrtest.read())

'''
'''seektest = open('/Users/suyayan/Downloads/py file operation/writetest.text',mode='r+',encoding='utf-8')
seektest.seek(6)
read =seektest.read()
print(read)

'''

#文件内容替换:
#要打开两份文件 > 第一份文件读取 > 修改后写入第二份文件 > 删除原始文件>重命名新文件
'''with open('/Users/suyayan/Downloads/py file operation/sb.text',mode='r+',encoding='utf-8') as sb1,open('/Users/suyayan/Downloads/py file operation/sb2.text',mode='w',encoding='utf-8') as sb2:
    for line in sb1:
        if 'yayan' in line:
            line=line.replace('yayan','guangjing')
        sb2.write(line)
import os
os.remove('/Users/suyayan/Downloads/py file operation/sb.text')
os.rename('/Users/suyayan/Downloads/py file operation/sb2.text','/Users/suyayan/Downloads/py file operation/sb.text')
'''


#文件操作&注册登录
'''
1:注册 
  
 （1）输入用户名
 （2）输入密码
 （3）打开文档，write
2:登录
  
'''
'''signname=input('请输入要注册的用户名：')
signpw=input('请设置密码：')
list=[]
with open('/Users/suyayan/Downloads/py file operation/signuptest.text',mode='w+',encoding='utf-8') as f:
    f.write('{} {}'.format(signname,signpw))
    f.seek(0)
    content = f.read()
    list = content.split()
    print(list)
    print('注册成功')
i=0
while i<3 :
    logname = input('请输入你的用户名：')
    logpw = input('请输入你的密码:')
    if logname == list[0] and logpw == list[1]:
        print('登录成功')
        break
    else:
        i+=1
        if 3-i ==0:
            print('登录失败，你已经失败3次，请稍后再试')
        else:print('登录失败，你还有{}次机会'.format(3-i))





with open('/Users/suyayan/Downloads/py file operation/signuptest.text',mode='r+',encoding='utf-8') as f1:
    content=f1.read()
    list=content.split()
    print(list)
'''


'''list=[1,'2','abc',4,5]
l2=list[:2]
'''
'''dic={'k1':'v1v1v1','k2':1234,'k3':233}
dic['k1']=dic['k1']+'v1v1v1'

print(dic)
'''

def func(*args,**kwargs):
    print('输入了')

func()

change