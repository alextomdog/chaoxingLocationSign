from api.api_proxy import API_PROXY
from api.uri import PPTSIGN
from utils import cookie_serialize


def sign_qrcode(
        cookies: dict[str, str],
        activeId: str | int,
        enc: str,
        longitude: float,
        latitude: float,
        altitude: float,
        address_name: str):

    api_proxy = API_PROXY(PPTSIGN)

    name = cookies["account_username"]
    fid = cookies["fid"]
    _uid = cookies["_uid"]
    query_string = f"?enc={enc}&name={name}&activeId={activeId}&uid={_uid}&clientip=&location={{\"result\":\"1\",\"address\":\"{address_name}\",\"latitude\":{latitude},\"longitude\":{longitude},\"altitude\":{altitude}}}&latitude=-1&longitude=-1&fid={fid}&appType=15"

    response = api_proxy.send_request(
        query_string=query_string,
        headers={
            "Cookie": cookie_serialize(cookies)
        }
    )
    return response.text
