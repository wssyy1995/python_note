
#程序一旦发生错误，就从错误的位置停下来了，不再继续执行后面的内容
'''ret=int(input('input a numnber:'))
print('ret:',ret)
'''

#上面这段代码如果用户输入一个字母，则会报错

#如何处理：
    #将可能出现异常的代码放到try里面，except后面跟对应的错误类型，except支持多个分支
    #try里一旦发生异常，处理之后会立即跳出try,不再try里执行下面的代码


'''try:
    ret = int(input('input a numnber:'))   #如果输入字母，发生ValueError
    print('ret:', ret)
    l = [1, 2, 4]
    l[8] = 3         #发生IndexError
    print(l)
except ValueError:
    print('你输入的内容有误，请输入一个数字')
except IndexError:
    print('你操作的列表索引超出范围')

'''



#万能异常 except Exception
    # 有了万能异常，也需要把能预测到的异常单独添加except分支
    # 万能异常应该放在所有异常分支的下面

'''try:
    ret = int(input('input a numnber:'))
    print('ret:', ret)
    l = [1, 2, 4]
    l[8] = 3
    print(l)
except ValueError:
    print('你输入的内容有误，请输入一个数字')
except Exception:
    print('发生异常啦')
'''

#else ：没有异常的时候，即try中所有代码成功执行，则执行else中的代码
'''try:
    ret = int(input('input a numnber:'))
    print('ret:', ret)
except ValueError:
    print('你输入的内容有误，请输入一个数字')
else:print('输入成功')
'''
#finnally: 不管try里的代码是否成功执行，都会执行finnally的代码
应用场景：在一个函数中，如果遇到return,finally会先执行，如果不用finnaly，会return之后会立即跳出函数

def func():
    try:
        f=open('file','w')
        return True
    except:
        return False
    finally:
        print('执行了finnally了')
        f.close()

print(func())



