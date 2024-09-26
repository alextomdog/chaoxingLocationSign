import time
from api.api_proxy import API_PROXY
from api.uri import ACTIVELIST
from utils import cookie_serialize


class ActivityStruct:
    def __init__(self):
        self.activity_id = None
        self.name = None
        self.courseId = None
        self.classId = None
        self.other_id = None

        self.status: bool = False
        self.msg: str = ""


def check_activity(cookies: dict[str, str], courseId: str, classId: str) -> ActivityStruct:
    api_proxy = API_PROXY(ACTIVELIST)
    activity_struct = ActivityStruct()

    current_time = int(time.time() * 1000)
    query_string = f"?fid=0&courseId={courseId}&classId={classId}&_={current_time}"
    headers = {
        "Cookie": cookie_serialize(cookies),
    }

    response = api_proxy.send_request(
        query_string=query_string, headers=headers)
    try:
        json_content = response.json()
    except Exception as e:
        activity_struct.status = False
        activity_struct.msg = response.text
        return activity_struct
    active_list = json_content["data"]["activeList"]
    # print(active_list)
    if len(active_list) > 0:
        # 获取最新的一次签到活动
        newest_activity = active_list[0]
        # 获取活动id
        try:
            other_id = int(newest_activity["otherId"])
        except Exception as e:
            activity_struct.status = False
            activity_struct.msg = "签到活动id获取失败"
            return activity_struct

        # 判断是否有效签到活动, newest_activity["status"]  判断是否超时
        if other_id >= 0 and other_id <= 5 and newest_activity["status"] == 1:
            # 如果超过一个小时，那么忽略这个活动
            # 获取当前时间（以毫秒为单位）
            current_time = int(time.time() * 1000)
            # 获取活动开始时间（以毫秒为单位）
            start_time = newest_activity["startTime"]
            # 检查活动是否开始超过半个小时（1800秒）
            if (current_time - start_time) / 1000 < 1800:
                activity_struct.status = True
                activity_struct.activity_id = newest_activity["id"]
                activity_struct.name = newest_activity["nameOne"]
                activity_struct.courseId = courseId
                activity_struct.classId = classId
                activity_struct.other_id = other_id
                activity_struct.msg = "检测到活动，准备签到"
            else:
                activity_struct.status = False
                activity_struct.msg = "活动已开始超过半个小时，主动忽略该活动"
            return activity_struct
        else:
            activity_struct.status = False
            activity_struct.msg = "检测到活动，但不是签到活动或者签到已经结束"
            return activity_struct
    else:
        activity_struct.status = False
        activity_struct.msg = "'请求似乎有些频繁，获取数据为空!'"
        return activity_struct


"""
{
    "result": 1,
    "msg": null,
    "data": {
        "ext": {
            "_from_": "245830363_105163423_150009988_f0eace2ac1404115da52117ea2dea794"
        },
        "readingDuration": 1,
        "activeList": [
            {
                "userStatus": 1,
                "nameTwo": "",
                "otherId": "4",
                "groupId": 2,
                "source": 15,
                "isLook": 1,
                "type": 2,
                "releaseNum": 0,
                "attendNum": 1,
                "activeType": 2,
                "logo": "https://mobilelearn.chaoxing.com/front/mobile/common/images/newActiveIcon80/active_type_2_gray.png?v=7",
                "nameOne": "签到",
                "startTime": 1726723626000,
                "id": 4000102558296,
                "endTime": 1726725426000,
                "status": 2,
                "nameFour": "09-19 13:57"
            },
            {
                "userStatus": 1,
                "nameTwo": "",
                "otherId": "3",
                "groupId": 2,
                "source": 15,
                "isLook": 1,
                "type": 2,
                "releaseNum": 0,
                "attendNum": 0,
                "activeType": 2,
                "logo": "https://mobilelearn.chaoxing.com/front/mobile/common/images/newActiveIcon80/active_type_2_gray.png?v=7",
                "nameOne": "签到",
                "startTime": 1726723570000,
                "id": 4000102558221,
                "endTime": 1726725370000,
                "status": 2,
                "nameFour": "09-19 13:56"
            },
            {
                "userStatus": 1,
                "nameTwo": "",
                "otherId": "0",
                "groupId": 2,
                "source": 15,
                "isLook": 1,
                "type": 2,
                "releaseNum": 0,
                "attendNum": 1,
                "activeType": 2,
                "logo": "https://mobilelearn.chaoxing.com/front/mobile/common/images/newActiveIcon80/active_type_2_gray.png?v=7",
                "nameOne": "签到",
                "startTime": 1726723508000,
                "id": 4000102558073,
                "endTime": 1726725308000,
                "status": 2,
                "nameFour": "09-19 13:55"
            }
        ]
    },
    "errorMsg": null
}
"""
