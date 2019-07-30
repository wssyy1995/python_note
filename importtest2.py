# it2=2
# print('this will run after imported,and run')
# def it22():
#     print('this is it22 function',it2)
#
# if __name__=='__main__':
#     print('this only run in importtest2.py')




import unittest
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name('hello','world')
        self.assertEqual(formatted_name,'Hello World') #一种断言，判断输入的结果是否与预期的结果相同

unittest.main()




def get_formatted_name(first,last):
    full_name=first+' '+last
    return full_name.title()


