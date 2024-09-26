from utils import cookie_serialize
from api.api_proxy import API_PROXY
from api.uri import PPTSIGN


class SignGeneralStruct:
    def __init__(self):
        self.msg = ""
        self.response_text = ""
        self.status = False


def sign_general(cookies: dict[str, str], activeId) -> SignGeneralStruct:
    api_proxy = API_PROXY(PPTSIGN)
    fid = cookies['fid']
    _uid = cookies['_uid']
    account_username = cookies['account_username']

    query_string = f"?activeId={activeId}&uid={_uid}&clientip=&latitude=-1&longitude=-1&appType=15&fid={fid}&name={account_username}"

    headers = {
        "Cookie": cookie_serialize(cookies)
    }

    response = api_proxy.send_request(
        query_string=query_string, headers=headers)

    sign_struct = SignGeneralStruct()
    sign_struct.response_text = response.text

    if "success" in response.text:
        sign_struct.msg = "签到成功"
        sign_struct.status = True
    elif "签到过了" in response.text:
        sign_struct.msg = "今天您已经签到过了"
        sign_struct.status = True
    else:
        sign_struct.msg = "签到失败"
        sign_struct.status = False
    return sign_struct
