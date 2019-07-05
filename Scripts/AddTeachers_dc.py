import unittest
from libs.tools import VerifyClass
from PO.MemberCenter.AddTeachers import AddTeacherClass


class TestAddTeacher(VerifyClass):
    def setUp(self):
        self.a = AddTeacherClass()

    def test_addteacher(self):
        result1,result2 = self.a.apiAddTeacher('13431720354','xiaohua','123456',0,5,'123','131666@163.com','13430120565',
                               '广东省','深圳市','龙岗区','这是详细地址','这是个人简介信息')
        self.verify_code(result1,200)
        self.verify_html(result2,'13431720354')

if __name__ == '__main__':
    unittest.main(verbosity=2)