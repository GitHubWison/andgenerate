# coding=utf-8
import httplib2
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
METHOD_GET = 'GET'
METHOD_POST = 'POST'
DEFAULT_HEADERS = {
    'Accept': 'application/json',
    'Authorization': 'Basic TWRzZC5QaGVwLkFwaTptZHNkLnBoZXAuYXBpLjIwMDUk',
    'UserName': 'amp6eDE=',
    'LoginName': 'amp6eDE=',
    'RequestSource': 'VmVoaWNsZUFwcA==',
    'Content-Type': 'application/json; charset=utf-8'
}


def init_url(url, params, method):
    if (method == METHOD_GET) & (len(params) != 0):
        #         将params直接拼接到ｕｒｌ后面
        url = '%s?' % (url)
        for key, value in params:
            url = '%s%s=%s&' % (url, key, value)
    return url


class Request:
    url = ''
    params = {}
    method = METHOD_GET
    headers = {}

    def __init__(self, url, params={}, method=METHOD_GET, headers=DEFAULT_HEADERS):
        self.url = init_url(url, params, method)
        self.params = params
        self.method = method
        self.headers = headers

    def request(self):
        h = httplib2.Http('.cache')
        response, content = h.request(self.url,
                                      self.method,
                                      str(self.params),
                                      headers=self.headers)
        print '请求地址：%s'%self.url
        print '请求参数：%s'%str(self.params)
        return content


# 格式化json字符串
class FormateJson:
    json_str = ''

    def __init__(self, json_str):
        self.json_str = json_str

    def pretty_json(self):
        result_str = json.dumps(json.loads(self.json_str), ensure_ascii=False, sort_keys=True, indent=2)
        return result_str
