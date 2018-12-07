import unittest

class Student(object):
    num = 1
    def __init__(self,name,age,score):
        self.id = Student.num
        Student.num = Student.num + 1
        self.name = name
        self.age = age
        self.score = score
        
class TestStudent(unittest.TestCase):
    def tect_init(self):
        print('tect_init')
        s1 = Student('xm',15,90)
        #认为两者之间是相等的
        self.assertEqual(s1.name,'隔壁小王')
        #判断这个括号内的表达式是否为真
        self.assertTrue(isinstance(s1.name,str))
        
    def tect_attr(self):
        print('tect_attr')
        s2=Student('xm',16,100)
        s2.score=100
        self.asserEqual(s2.score,100)
        
if __name__=='__main__':
     unittest.main()