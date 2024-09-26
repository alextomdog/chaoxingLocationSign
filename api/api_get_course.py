import re
from api.uri import COURSELIST
from api.api_proxy import API_PROXY


class CourseListStruct:
    def __init__(self):
        self.status: bool = False
        self.course_list: list[CourseInfoStruct] = []
        self.msg: str = ""


class CourseInfoStruct:
    def __init__(self, courseId: str, classId: str, courseName: str, teacherName: str):
        self.courseId = courseId
        self.classId = classId
        self.courseName = courseName
        self.teacherName = teacherName

    def __str__(self):
        return f"CourseId: {self.courseId}, ClassId: {self.classId}, CourseName: {self.courseName}, TeacherName: {self.teacherName}"


def get_courses_wrapper(_uid: str, _d: str, vc3: str):

    api_proxy = API_PROXY(COURSELIST)
    headers = {
        "Accept": "text/html, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",  # 服务器支持 gzip 压缩时自动处理
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"_uid={_uid}; _d={_d}; vc3={vc3}"
    }
    data = {
        'courseType': '1',
        'courseFolderId': '0',
        'courseFolderSize': '0'
    }
    response = api_proxy.send_request(headers=headers, data=data)
    return response


def extract_course_info(html_data):
    # 定义正则表达式，匹配每个li标签中的courseId, classId, course-name和teacher name
    pattern = re.compile(r'<li class="course clearfix" courseId="(?P<courseId>\d+)" clazzId="(?P<classId>\d+)"[^>]*>.*?'
                         r'<span class="course-name overHidden2" title="(?P<courseName>[^"]+)">.*?</span>.*?'
                         r'<p class="line2" title="(?P<teacherName>[^"]+)">', re.S)

    # 查找所有匹配的结果
    courses = []
    for match in pattern.finditer(html_data):
        course_info = {
            'courseId': match.group('courseId'),
            'classId': match.group('classId'),
            'courseName': match.group('courseName'),
            'teacherName': match.group('teacherName')
        }
        courses.append(CourseInfoStruct(**course_info))

    return courses


def get_course(cookies: dict) -> CourseListStruct:
    course_struct = CourseListStruct()
    params = {
        "_uid": cookies["_uid"],
        "_d": cookies["_d"],
        "vc3": cookies["vc3"],
    }
    response = get_courses_wrapper(**params)
    if response.ok:
        html_content = response.text
        course_struct.course_list = extract_course_info(html_content)
        course_struct.status = True
        course_struct.msg = "Success"
        return course_struct
    else:
        course_struct.msg = f"Error: {response.status_code}"
        course_struct.status = False
        return course_struct
