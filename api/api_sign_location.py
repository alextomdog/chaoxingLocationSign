from api.uri import PPTSIGN
from api.api_proxy import API_PROXY
from utils import cookie_serialize


class SignLocationStruct:
    def __init__(self):
        self.msg = ""
        self.response_text = ""
        self.status = False


def sign_location(cookies: dict[str, str], activeId: str | int, address_name: str, longitude: float, latitude: float):
    """
    签到位置
    :param address_name: 签到地址名称
    :param longitude: 经度
    :param latitude: 纬度
    :return:
    """
    account_name = cookies["account_username"]
    fid = cookies["fid"]
    _uid = cookies["_uid"]

    api_proxy = API_PROXY(PPTSIGN)
    sign_location_struct = SignLocationStruct()

    query_string = f"?name={account_name}&address={address_name}&activeId={activeId}&uid={_uid}&clientip=&latitude={latitude}&longitude={longitude}&fid={fid}&appType=15&ifTiJiao=1"

    headers = {
        "Cookie": cookie_serialize(cookies)
    }

    response = api_proxy.send_request(
        headers=headers, query_string=query_string)

    if "success" in response.text:
        sign_location_struct.status = True
        sign_location_struct.msg = "签到成功"
    elif "签到过了" in response.text:
        sign_location_struct.status = True
        sign_location_struct.msg = "今天您已经签到过了"
    else:
        sign_location_struct.status = False
        sign_location_struct.msg = "签到失败"

    return sign_location_struct
