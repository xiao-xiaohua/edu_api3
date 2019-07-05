from libs.tools import BaseHttp


#继承BaseHttp
class LoginClass(BaseHttp):
    cookies = {'PHPSESSID':''}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    def apiLogin(self, username, passsword):
        # 将接口url拆分成了host和url，host封装在tools里
        url = '/admin.php?m=mgr/admin.chklogin&ajax=1'
        # 登录传参
        login_data = {
            'username': username,
            'password': passsword,
        }
        result = self.http_send(url=url, data=login_data, headers=self.headers)
        pid = result.cookies['PHPSESSID']
        self.cookies['PHPSESSID'] = pid
        return result


if __name__ == '__main__':
    run = LoginClass()
    result = run.apiLogin('admin',
                          'admin')
    print(result.text)
    print(run.cookies)


