from utils import cookie_serialize
from api.uri import PRESIGN
from api.api_proxy import API_PROXY


def loading_sign_page(cookies: dict[str, str], activeId, classId, courseId) -> None:
    api_proxy = API_PROXY(PRESIGN)
    _uid = cookies.get("_uid")
    query_string = f"?courseId={courseId}&classId={classId}&activePrimaryId={activeId}&general=1&sys=1&ls=1&appType=15&tid=&uid={_uid}&ut=s"
    headers = {
        "Cookie": cookie_serialize(cookies)
    }
    response = api_proxy.send_request(
        headers=headers, query_string=query_string)

    # 获得的是请求签到按钮，详情见 /temp/api_sign_pre.html
    return None
