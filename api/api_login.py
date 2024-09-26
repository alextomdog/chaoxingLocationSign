from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import binascii
from api.api_proxy import API_PROXY
from api.uri import LOGIN


class LoginStruct:
    def __init__(self):
        self.status: bool = False
        self.data: dict | None = None
        self.msg: str | None = None


def encrypt_password(password):
    key = b'u2oh6Vu^'
    cipher = DES.new(key, DES.MODE_ECB)
    padded_password = pad(password.encode('utf-8'), DES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    return binascii.hexlify(encrypted_password).decode()


def login(username, password) -> LoginStruct:

    login_struct: LoginStruct = LoginStruct()

    api_login_proxy = API_PROXY(LOGIN)

    # 初始化默认参数
    DefaultParams = {
        'fid': '-1',
        'pid': '-1',
        'refer': 'http%3A%2F%2Fi.chaoxing.com',
        '_blank': '1',
        't': True,
        'vc3': '',
        '_uid': '',
        '_d': '',
        'uf': '',
        'lv': ''
    }

    formdata = {
        'uname': username,
        'password': password,
        'fid': '-1',
        't': 'true',
        'refer': 'https%253A%252F%252Fi.chaoxing.com',  # URL encoded
        'forbidotherlogin': '0',
        'validate': ''
    }

    # 设置请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
    }

    # 发送POST请求
    response = api_login_proxy.send_request(headers=headers, data=formdata)

    # 处理结果
    if response.status_code == 200:
        result = response.json()  # 假设返回的结果是JSON
        if result['status'] == True:
            # 获取 "Set-Cookie" 头
            cookies = response.headers.get('Set-Cookie')

            cookie_map = {}

            if not cookies:
                login_struct.msg = "网络异常，换个环境重试, AuthFailed"
                login_struct.status = False
                return login_struct

            cookie_list = cookies.split(',')  # 多个cookie可能以逗号分隔

            for cookie in cookie_list:
                c_equal = cookie.find('=')
                c_semi = cookie.find(';')
                item_name = cookie[:c_equal].strip()
                item_value = cookie[c_equal + 1:c_semi].strip()
                cookie_map[item_name] = item_value

            # 合并 cookie 到默认参数中
            rt_cookies = {**DefaultParams, **cookie_map}
            login_result = rt_cookies

            # 输出结果
            login_struct.msg = "登录成功"
            login_struct.status = True
            login_struct.data = login_result
            return login_struct

        else:
            login_struct.msg = "登录失败"
            login_struct.status = False
            return login_struct
    else:
        login_struct.msg = f"Request failed with status code: {response.status_code}"
        login_struct.status = False
        return login_struct
