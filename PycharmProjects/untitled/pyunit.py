import requests
import json
def test_admin_user_login(self):
    """
    测试用户登录
    by:Harmo
    :return:
    """

    url = "%s%s" % (self.base_url, '/task/admin-user-login/')

    params = dict(
        user='admin',
        password='222222',

    )

    res = requests.post(url, data=params)
    print (res.text)

    res_dict = json.loads(res.text)
    self.assertEqual(res_dict['code'], 200)