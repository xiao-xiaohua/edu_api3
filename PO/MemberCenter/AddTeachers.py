
from libs.basework import LoginClass

class AddTeacherClass(LoginClass):
    def apiAddTeacher(self,username,realname,password,sex,roleid,orid1,email,phone,location_p,location_c,location_a,address,introduce,type=1):
        url_addteacher = '/admin.php?m=mgr/member2.saveMemberInfo&id='
        data_addteacher = {'username':username,
                'realname':realname,
                'password':password,
                'sex':sex,
                'roleid':roleid,
                'orid1':orid1,
                'email':email,
                'phone':phone,
                'location_p':location_p,
                'location_c':location_c,
                'location_a':location_a,
                'address':address,
                'introduce':introduce,
                'type':type
        }

        run = LoginClass()
        run.apiLogin('admin','admin')
        #添加教师接口请求
        result1 = self.http_send(url=url_addteacher,data=data_addteacher,cookies=self.cookies)
        #校验是否添加成功
        url_teacherlist = '/admin.php?m=mgr/member2.memberlist&type=1'
        result2 = self.http_send(method='get',url=url_teacherlist,cookies=self.cookies)
        return result1,result2



if __name__ == '__main__':
    run = AddTeacherClass()
    result1,result2 = run.apiAddTeacher('13430120560','Angle','123456',0,5,'123','131666@163.com','13430120565',
                               '广东省','深圳市','龙岗区','这是详细地址','这是个人简介信息')
    print(result1.status_code)
    # print(result1.json())    报错，怎么处理？
    print(result2.text)