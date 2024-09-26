from api import sign_location
from api import loading_sign_page
from api import check_activity
from api import get_course
from api import login
from api import get_account_username

username = "18888888888"  # 手机号
password = "**********"  # 密码

# https://api.map.baidu.com/lbsapi/getpoint/

# 思学楼c区定位坐标
location_geography = '104.19107,30.827562'

# 博学楼B区定位坐标
# location_geography = '104.192916,30.828876'


longitude = float(location_geography.split(',')[0])
latitude = float(location_geography.split(',')[1])


address_name = "中国四川省成都市新都区新都街道南环路"


result = login(username, password)

print(f'用户 {username}: {result.msg}')

if result.status:
    account_username = get_account_username(result.data)
    result.data["account_username"] = account_username
    cookies = result.data
else:
    exit()

courseList = get_course(cookies).course_list

for index, course in enumerate(courseList):
    print(index+1, ":", course.courseName, " ", course.teacherName)


selected_course = input("请输入要签到的课程的序号: ")
try:
    course = courseList[int(selected_course)-1]
except Exception as e:
    exit()
    
# # 获取这个课程的签到的活动的信息
activity_result = check_activity(
    cookies, course.courseId, course.classId)

if activity_result.status == False:
    print(course, "没有签到活动")
    print(activity_result.msg)
else:
    print(course, "有签到活动")
    activity_id = activity_result.activity_id
    courseId = activity_result.courseId
    classId = activity_result.classId
    msg = activity_result.msg

    loading_sign_page(cookies, activity_id, classId, courseId)

    sign_location_response = sign_location(
        cookies, activity_id, address_name, longitude, latitude)
    if sign_location_response.status == False:
        print(sign_location_response.response_text)
        print(sign_location_response.msg)
    else:
        print(sign_location_response.msg)
