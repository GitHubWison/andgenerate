# coding=utf-8
import os
import datetime
import sys
import xlwt

time_format = '%Y-%m-%d'
start_time_key = 'start_time'
end_time_key = 'end_time'
wb = xlwt.Workbook(encoding='utf-8')

ws = wb.add_sheet('test_sheet')


# style = xlwt.XFStyle()
# font = xlwt.Font()
# font.name = 'SimSun'
# style.font = font

# path:本地svn路径
def export_svn_log(svn_local_path):
    # 切换到本地svn路径去
    os.chdir(svn_local_path)
    print os.getcwd()
    end_time = datetime.datetime.now()+datetime.timedelta(days=1)
    start_time = end_time + datetime.timedelta(days=-5)
    start_end_time = get_date_range(start_time, end_time)
    print '%s:%s' % ('开始时间', start_end_time[start_time_key])
    print '%s:%s' % ('结束时间', start_end_time[end_time_key])
    svn_check_log_str = 'svn log -r {%s}:{%s}' % (start_end_time[start_time_key], start_end_time[end_time_key])
    print svn_check_log_str
    fp = os.popen(svn_check_log_str, 'r')
    svn_log = fp.read()
    os.chdir(sys.path[0])
    with open('output/svnlog.txt', 'w')as file_obj:
        file_obj.write(svn_log)
    build_excel(get_log())


def build_excel(list):
    for index, item in enumerate(list):
        ws.write(index, 0, item)
    wb.save('output/test.xls')


# 提取log中的信息
def get_log():
    get_date_flag = False
    log_list = []
    file = open('output/svnlog.txt', 'r')
    line = file.readline()
    while line:
        line = file.readline()
        if len(line) > 4:
            last_str = line[-5:]
            if last_str == 'line\n':
                get_date_flag = True
                continue
            elif last_str == '----\n':
                get_date_flag = False
                continue
        if get_date_flag:
            if line != '\n':
                line_temp = line.replace('\n', '')
                log_list.append(line_temp)
    return log_list


# 获得日期范围
# start_time:开始时间
# end_time:结束时间
def get_date_range(start_time, end_time):
    formated_start_t = start_time.strftime(time_format)
    formated_end_t = end_time.strftime(time_format)
    return {start_time_key: formated_start_t, end_time_key: formated_end_t}


export_svn_log('/home/xuqiwei/documents/android/project/svn/WisdomAidApp/trunk/WisdomAidApp')
# build_excel()
# get_log()
