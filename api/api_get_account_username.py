from .uri import ACCOUNTMANAGE
from .api_proxy import API_PROXY
from utils import cookie_serialize


def extract_name(data):
    end_of_messageName = data.find('messageName') + 20
    name = data[end_of_messageName: data.find('"', end_of_messageName)]
    return name


def get_account_username(cookies) -> str:
    api_proxy = API_PROXY(ACCOUNTMANAGE)
    headers = {
        "Cookie": cookie_serialize(cookies),
    }
    response = api_proxy.send_request(headers=headers)
    response.encoding = "utf-8"
    return extract_name(response.text)
