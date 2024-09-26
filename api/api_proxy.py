import requests


class API_PROXY:
    def __init__(self, proxy):
        self.__proxy = proxy

        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
        }

    def send_request(self, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        else:
            kwargs["headers"].update(self.headers)

        if "query_string" in kwargs:
            self.__proxy["URL"] += kwargs["query_string"]
            del kwargs["query_string"]

        # print(self.__proxy["URL"])

        if self.__proxy["METHOD"] == 'GET':
            return requests.get(self.__proxy["URL"], **kwargs)
        elif self.__proxy["METHOD"] == 'POST':
            return requests.post(self.__proxy["URL"], **kwargs)
