# coding=utf-8
import http_request
import os


# request = http_request.Request('http://172.16.23.14:45200/api/mobilemedicalrecord/getmedicalrecordbypatientid/8ee5daa6-ba26-4d17-83b3-eda99ea443ad?AppId=PreHospitalCare')
# request = http_request.Request('http://172.16.23.14:4500/api/Public/CheckUserIsValidWithCarInfo',
#                                method=http_request.METHOD_POST, params={"AppId": "PreHospitalCare", "LoginName": "pad",
#                                                                         "Password": "202CB962AC59075B964B07152D234B70",
#                                                                         "PlateNumber": "6IuPRSAwQTEyNQ=="}
#                                )
# json_res = http_request.FormateJson(request.request())
# pretty_json = json_res.pretty_json()
# # print pretty_json
# file_object = open('outputs/result.txt', 'w')
# file_object.write(pretty_json)
# os.system('xdg-open outputs/result.txt')
def get_test(url, method=http_request.METHOD_GET, params={}):
    request = http_request.Request(url, params=params, method=method)
    json_res = http_request.FormateJson(request.request()).pretty_json()

    file_object = open('format_json/outputs/result.txt', 'w')
    file_object.write(json_res)
    os.system('xdg-open format_json/outputs/result.txt')
    return json_res

# print get_test('http://www.tngou.net/api/info/classify')
