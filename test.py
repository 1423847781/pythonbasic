import unittest

class Student(object):
    num = 1
    def __init__(self,name,age,score):
        self.id = Student.num
        Student.num = Student.num + 1
        self.name = name
        self.age = age
        self.score = score

class TestDict(unittest.TestCase):
    def test_init(self):
        print('test_init')
        s1 = self.s1
        #认为两者之间是相等的
        self.assertEqual(s1.name,'xm')
        #判断这个括号内的表达式是否为真
        self.assertTrue(isinstance(s1.name,str))
    def test_attr(self):
        s2 = self.s1
        s2.score = 100
        self.assertEqual(s2.score,100)
        print('test_attr')
        self.abc()
    def abc(self):
        return '123'
    def test_xx(self):
        print('test_xx')
        s1 = self.s1
        self.assertTrue(isinstance(s1.age,int))
    def setUp(self):
        #用于每一次都需要初始化的一些执行内容
        #将测试环境初始化出来
        self.s1 = Student('xm',15,90)
        print(self.s1)
        print('setUp...')

    def tearDown(self):

        #将测试环境恢复到最初的状态
        self.s1 = None
        print('tearDown...')
        

# if __name__ == '__main__':
#     unittest.main()