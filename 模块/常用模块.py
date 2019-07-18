
#正则表达式：
    '''字符组:一个人字符组只能匹配一个人字符
    []：字符组，规定一个字符位子上能出现的字符
    [0-9]：0-9所有数字都能匹配上
    [a-z]:a-z所有小写字母
    [0-9a-zA-Z]：一个字符组内可以有多种匹配规则
    [^a] ：字符组加一个尖角号，相当于非




    原字符：
        .  匹配除换行符以外的任意字符

        \w  匹配字符或数字或下划线

        \s 匹配任意的空白符 （\S则为非）

        \d  匹配任意数字    （\D则为非）

        \W （大写）匹配非字符或数字或下划线

        \n  匹配一个换行符

        \t 匹配一个制表符tab

    #重要
        ^   匹配字符串的开始
        $   匹配字符串的结尾  例子:^[0-9][a-z]$，只能匹配5a,2r,9g这种结果
        |   匹配字符a或字符b
        ()  分组



    #上面都是单个字符的匹配，如需要匹配一串字符，需要量词

    量词:量词需要匹配的正则规则后面，且这个人量词只约束紧贴着这个量词的规则

        *   匹配0次或多次
        +   匹配1次或多次
        ?   匹配0次或1次
        {n} 重复n次
        {n,} 重复n此或更多次
        {n,m}  重复n到m次,默认贪婪匹配

        量词后面加？则表示非贪婪匹配
        贪婪匹配：从要匹配的字符开始一直找找找找到最后，再回溯回去到需要停止的字符
        非贪婪匹配：先把要停止的字符位置找到，只要一找到这个字符就结束





    分组
        ()需要进行整体约束的时候
        例如：([abc][123])+
        '''




#re模块
re.findall('正则表达式'，'内容')  #返回所有满足匹配条件的结果，放在列表中
    ret = re.findall('[abc][123]','a3rj8')
    findall分组优先，如果取消分组优先的话，需要在前面加上?:

re.search('b','abcabcacb').group()   #从前往后，寻找到第一个符合的结果，并调用group()才能将结果返回,如果找不到，则返回none，调用group()会报错
    返回第一个b
re.match('b','abcabcacd').group()      #从头开始匹配，如果从头开始匹配得上，就返回一个人变量，匹配的内容用group()返回，否则返回none，调用group()会报错

re.sub('正则表达式'，'要替换的新内容'，'原内容',参数1表示只替换一次)
s='a4g91231g023'
s1=re.sub('([a-z][0-9])','sub',s) ,替换不需要加两次


#collection模块
    from collections import namedtuple
    Point=namedtuple('point',['x','y','z'])
    p1=Point(1,2,3)
    print(p1.x)

    import queue
    q = queue.Queue()
    q.put(10)
    q.put(5)
    q.put(15)
    print(q.get())

    from collections import deque  # 双端队列，可以从前后取数据
    dq = deque(['a', 'b', 'c'])  #先创建一个双端队列对象
    dq.append(2)  # 从后面放数据
    dq.appendleft()  # 从前面放数据
    dq.pop()  # 从后面取数据
    dq.popleft()  # 从前面取数据
    dq.insert(索引，插入的值)


#time模块
    import time
    time.sleep(一个以秒为单位的时间长度)
    time.time() 从1970年1月1日0点开始按秒计算

    表示时间的三种方式：
        时间戳时间：float时间，给计算机看的
        time.time()

        字符串：格式化时间，给人看的
        print(time.strftime('%Y/%m/%d %H:%M:%S'))



        结构化时间：元祖，计算用的
        t1=time.localtime(time.time())  #将时间戳转化为结构化时间
        t2=time.strptime('2000/12/31 19:00:00','%Y/%m/%d %H:%M:%S')  将格式化时间转换为结构化时间
        time.mktime(t1/t2)  #将结构化时间转化为时间戳时间

    例子：计算时间差
        import time
        true_time=time.mktime(time.strptime('2017-08-12 08:30:00','%Y-%m-%d %H:%M:%S'))  #将格式化时间转化为结构化时间再转化为时间戳
        time_now=time.mktime(time.strptime('2019-08-12 11:00:00','%Y-%m-%d %H:%M:%S'))
        dif_time=time_now-true_time #两个时间相差的时间戳
        print(dif_time)
        struct_time=time.gmtime(dif_time) #将相差的时间戳转换为utc时区的struc_time，也就是从1970年1月1日0点往后加上该时间戳
        print(struct_time)
        print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                               struct_time.tm_mday-1,struct_time.tm_hour,
                                               struct_time.tm_min,struct_time.tm_sec))





#random模块
    import random
    随机小数
        random.random()  #大于0小于1之间的小数
        random.uniform(1,2) #大约1小于2的小数
    随机整数
        random.randint(1,5) #大于等于1且小于等于5之间的整数
        random.randrange(1,10,2) #大于等于1且小于10之间的奇数

    随机选择一个返回
        random.choice(可迭代对象)  #随机返回该可迭代对象中的一个元素
        random.sample([12,34,56],2) #列表元素（元祖或集合也可以，字典不可以）任意两个组合

    打断列表顺序
        random.shuffle([1,2,4,3])
        例子：随机生成一个验证码
        import random
        s=''
        for i in range(5):
            letter = chr(random.randint(65, 90))
            num = random.randint(0, 9)
            l = [letter, num]
            s=s+str(random.choice(l))
        print(s)


#os模块
    os.getcwd() 获取当前工作母，即当前python脚本工作的目录
    os.chdir(r'路径')  改变当前脚本工作目录
    os.makedirs('dirname1/dirname2')  创建多层递归文件夹
    os.removedirs('dirname1')  指定删除一个目录，回到上层目录，如果上层变为空了，也删除，直到遇到不为空的目录
    os.mkdir('dirname') 生成单层目录
    os.listdir('dirname')  列出该目录下所有的子目录和文件
    os.stat('dirname')  查看该目录的信息
    os.system('ls')   运行操作系统命令，直接显示

    os.path.isfile('path')/isdir('path')


#sys模块：sys模块是与python解释器交互的一个接口
    sys.exit(0/1)  正常退出时exit(0),错误退出exit(1)
    sys.argv  命令行参数list,第一个元素是程序本身路径
    sys.version  获取python 解释程序的版本信息
    sys.path 返回模块的搜索路径
    sys.platform 返回操作系统平台名称




#序列化模块 ：将原本的字典，列表等内容转化成字符串的过程称为序列化
    序列就是字符串

    必须要转成字符串的应用场景：写文件，在网络上传输的时候

    从字符串再转回数据类型的过程--反序列化

    三种序列化模块
    #一.json :
        #通用的序列化格式
        #只有很少的一部分数据类型能够通过json转化成字符串

    (1)dumps序列化方法
    dic={'k1':'v1','k2':'v2'}
    print(type(dic),dic)
    import json
    str_d=json.dumps(dic)
    print(type(str_d),str_d)
    #json中所有引号都会转换成双引号


    (2)loads反序列化方法
    dic_d=json.loads(str_d)
    print(dic_d)

    能够序列化的数据格式：数字，字符串，字典，列表

(3) dump,load (先将数据类型序列化，在写入文件中)
    dic={'k1':'v1','k2':'v2'}
    f=open('jumptest','w',excoding='utf-8')
    json.dump(dic,f)
    f.close()
    f=open('jumptest')
    res.json.load(f)
    print(type(res),res)

    如果写入中文的话
    json，dump(dic,f,ensure_ascii=False)



    #pickle
        #所有的python中的数据类型都可以转化成字符串形式
        #pickle序列化的内容只有python能理解
        #且部分反序列化依赖python代码

        jumps,loads,jump,load方法与json相同，并可以操作json不能操作的数据类型
        pickle序列化之后是bytes类型，所以open file，是需要用rb和wb
        pickle支持分次load，json只能一次dump,一次性load




    #shelve
        #操作简单，使用序列化句柄直接操作
        f=shelve.open('jumptest')
        f['key']={'int':10,'float':9.5}
        f.close()




