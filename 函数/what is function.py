#len(s)

#(1）初始函数，无参数

s='abcdefghijklmn'
def my_len():
    i = 0
    for j in s :
        i+=1
    print(i)
    return(i)
    #return执行后自动跳出函数，不再执行下面的语句
    print('after return')

length=my_len(4)
print(length)








