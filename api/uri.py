LOGIN_PAGE = {
    'URL': 'https://passport2.chaoxing.com/mlogin?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com',
    'METHOD': 'GET'
}

LOGIN = {
    'URL': 'https://passport2.chaoxing.com/fanyalogin',
    'METHOD': 'POST'
}

PRESIGN = {
    'URL': 'https://mobilelearn.chaoxing.com/newsign/preSign',
    'METHOD': 'GET'
}

ANALYSIS = {
    'URL': 'https://mobilelearn.chaoxing.com/pptSign/analysis',
    'METHOD': 'GET'
}

ANALYSIS2 = {
    'URL': 'https://mobilelearn.chaoxing.com/pptSign/analysis2',
    'METHOD': 'GET'
}

PPTSIGN = {
    'URL': 'https://mobilelearn.chaoxing.com/pptSign/stuSignajax',
    'METHOD': 'GET'
}

PPTACTIVEINFO = {
    'URL': 'https://mobilelearn.chaoxing.com/v2/apis/active/getPPTActiveInfo',
    'METHOD': 'GET'
}

COURSELIST = {
    'URL': 'https://mooc1-1.chaoxing.com/visit/courselistdata',
    'METHOD': 'POST'
}

BACKCLAZZDATA = {
    'URL': 'https://mooc1-api.chaoxing.com/mycourse/backclazzdata',
    'METHOD': 'GET'
}

ACTIVELIST = {
    'URL': 'https://mobilelearn.chaoxing.com/v2/apis/active/student/activelist',
    'METHOD': 'GET'
}

ACCOUNTMANAGE = {
    'URL': 'https://passport2.chaoxing.com/mooc/accountManage',
    'METHOD': 'GET'
}

PANCHAOXING = {
    'URL': 'https://pan-yz.chaoxing.com',
    'METHOD': 'GET'
}

PANLIST = {
    'URL': 'https://pan-yz.chaoxing.com/opt/listres',
    'METHOD': 'POST'
}

PANTOKEN = {
    'URL': 'https://pan-yz.chaoxing.com/api/token/uservalid',
    'METHOD': 'GET'
}

PANUPLOAD = {
    'URL': 'https://pan-yz.chaoxing.com/upload',
    'METHOD': 'POST'
}

WEBIM = {
    'URL': 'https://im.chaoxing.com/webim/me',
    'METHOD': 'GET'
}

# 无课程的群聊的一些 API
CHAT_GROUP = {
    'PRESTUSIGN': {
        'URL': 'https://mobilelearn.chaoxing.com/sign/preStuSign',
        'METHOD': 'GET'
    },
    'SIGN': {
        'URL': 'https://mobilelearn.chaoxing.com/sign/stuSignajax',
        # 也存在是 POST 的情况
        'METHOD': 'GET'
    }
}
