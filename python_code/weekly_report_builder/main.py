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
basic_unit = 20

borders_test = xlwt.Borders()
borders_test.left = 1
borders_test.right = 1
borders_test.bottom = 1
borders_test.top = 1

mission_catagory = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
before_days = -10

end_time = datetime.datetime.now() + datetime.timedelta(days=1)
start_time = end_time + datetime.timedelta(days=before_days)


# style = xlwt.XFStyle()
# font = xlwt.Font()
# font.name = 'SimSun'
# style.font = font

# svn_remote_path:远程svn路径
# svn_username:svn用户名
def export_svn_log(svn_remote_path, svn_username):
    # 切换到本地svn路径去
    # os.chdir(svn_local_path)
    # print os.getcwd()
    start_end_time = get_date_range(start_time, end_time)
    print '%s:%s' % ('开始时间', start_end_time[start_time_key])
    print '%s:%s' % ('结束时间', start_end_time[end_time_key])
    svn_check_log_str = 'svn log -r {%s}:{%s} --search %s %s' % (start_end_time[start_time_key],
                                                                 start_end_time[end_time_key], svn_username,
                                                                 svn_remote_path)
    print svn_check_log_str
    fp = os.popen(svn_check_log_str, 'r')
    svn_log = fp.read()
    os.chdir(sys.path[0])
    with open('output/svnlog.txt', 'w')as file_obj:
        file_obj.write(svn_log)
    build_excel(get_log())


def build_excel(list):
    # 初始化表格
    init_excel()
    missions_dic = div_missions(list)
    index = 0
    flag_start_index = 2
    for total_index, total_item in enumerate(mission_catagory):
        # 每天的任务列表
        everyday_mission_list = missions_dic[total_item]

        # 每天的任务个数
        everyday_mission_len = len(everyday_mission_list)
        flag_end_index = flag_start_index + everyday_mission_len - 1
        # 合并纵向的单元格
        print '%s===%s===%s' % (flag_start_index, flag_end_index, total_item)
        style_test4 = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index black,'
                                  'bold on,italic off;align:wrap on,vert center,horiz center;')
        style_test4.borders = borders_test
        ws.write_merge(flag_start_index, flag_end_index, 1, 1, total_item, style_test4)
        flag_start_index = flag_end_index + 1
        avg_hour = 8 / everyday_mission_len
        mod_hour = 8 % everyday_mission_len
        for every_index, item in enumerate(everyday_mission_list):
            # for index, item in enumerate(list):
            ws.row(index + 2).height = 400

            style_test3 = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index black,'
                                      'bold off,italic off;align:wrap on,vert center,horiz center;')  # 填写id
            style_test3.borders = borders_test
            ws.write(index + 2, 0, index + 1, style_test3)

            style_test2 = xlwt.easyxf('font:height 220,name SimSun,color_index black,'
                                      'bold off,italic off;align:wrap on,vert center,horiz center;')  # 填写类型
            style_test2.borders = borders_test
            ws.write(index + 2, 2, '新产品研发', style_test2)

            style_test1 = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index black,'
                                      'bold off,italic off;align:wrap on,vert center,horiz left;')  # 填写任务名称
            style_test1.borders = borders_test
            ws.write(index + 2, 3, item, style_test1)
            # style_test1.alignment.horz = xlwt.Alignment.HORZ_RIGHT
            if everyday_mission_len - 1 == every_index:
                ws.write(index + 2, 4, avg_hour + mod_hour, style_test1)
            else:
                ws.write(index + 2, 4, avg_hour, style_test1)

            style_test = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index brown,'
                                     'bold on,italic off;align:wrap on,vert center,horiz center;'
                                     'pattern: pattern solid,fore_colour light_green;')
            style_test.borders = borders_test
            #     填写完成状况
            ws.write(index + 2, 5, '100%', style_test)

            # 备注
            ws.write(index + 2, 6, '', style_test1)
            index += 1
    # 下周工作计划
    index += 2
    style_next_week = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index black,'
                                  'bold on,italic off;align:wrap on,vert center,horiz center;'
                                  'pattern: pattern solid,fore_colour gray25;')
    style_next_week.borders = borders_test
    ws.row(index).height = 540
    ws.write_merge(index, index, 1, 5, '下周工作计划', style_next_week)
    ws.write(index, 0, 'ID', style_next_week)
    ws.write(index, 6, '计划工时', style_next_week)
    index += 1
    style_next_week_content = xlwt.easyxf('font:height 220,name Microsoft YaHei,color_index black,'
                                          'bold off,italic off;align:wrap on,vert center,horiz center;')
    style_next_week_content.borders = borders_test
    ws.write(index, 0, '1', style_next_week_content)
    ws.write_merge(index, index, 1, 5, '', style_next_week_content)
    ws.write(index, 6, '', style_next_week_content)
    wb.save('output/test.xls')


def init_excel():
    start_end_time = get_date_range(start_time, end_time)
    ws.row(0).height = 800
    title_name = '个人工作任务跟踪表(%s至%s)' % (start_end_time[start_time_key], start_end_time[end_time_key])

    title_style = xlwt.easyxf('font:height 360,name Microsoft YaHei,color_index black,'
                              'bold on,italic off;align:wrap on,vert center,horiz center;'
                              'pattern: pattern solid,fore_colour light_orange')
    title_style.borders = borders_test
    ws.write_merge(0, 0, 0, 6, title_name, title_style)
    ws.row(1).height = 915
    ws.col(0).width = 1500
    ws.col(3).width = 20000
    capture_style = ('font:height 220,name Microsoft YaHei,color_index black,'
                     'bold on,italic off;align:wrap on,vert center,horiz center;'
                     'pattern: pattern solid,fore_colour pale_blue')
    cap_style = xlwt.easyxf(capture_style)
    cap_style.borders = borders_test
    ws.write(1, 0, 'ID', cap_style)
    ws.write(1, 1, '时间', cap_style)
    ws.write(1, 2, '类型', cap_style)
    ws.write(1, 3, '任务名称', cap_style)
    ws.write(1, 4, '实际工时', cap_style)
    ws.write(1, 5, '完成状态', cap_style)
    ws.write(1, 6, '备注', cap_style)


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


# 拆分任务
# mission_catagory:任务区分
def div_missions(mission_list):
    # 分类列表的长度
    catagory_len = len(mission_catagory)
    # 任务列表的长度
    mission_list_len = len(mission_list)
    # 每个分类下的任务个数
    each_catagory_len = mission_list_len / catagory_len
    # 余下的任务个数
    remain_missions = mission_list_len % catagory_len
    # 整合后的missionlist
    result_missiondic = {}
    each_start_list_index = 0
    # each_end_list_index = 0
    for index, item in enumerate(mission_catagory):
        each_end_list_index = each_start_list_index + each_catagory_len
        if remain_missions != 0:
            each_end_list_index += 1
            remain_missions -= 1
        result_missiondic[mission_catagory[index]] = mission_list[each_start_list_index:each_end_list_index]
        each_start_list_index = each_end_list_index
    return result_missiondic


# 获得日期范围
# start_time:开始时间
# end_time:结束时间
def get_date_range(start_time, end_time):
    formated_start_t = start_time.strftime(time_format)
    formated_end_t = end_time.strftime(time_format)
    return {start_time_key: formated_start_t, end_time_key: formated_end_t}


# export_svn_log('https://svn.mdsd.cn:7443/svn/PreHospitalEmergency/trunk/AndroidApp/WisdomAidApp/trunk/WisdomAidApp',
#                'CP-xuqiwei')
export_svn_log('https://svn.mdsd.cn:7443/svn/PreHospitalEmergency/trunk/高危筛查/Src',
               'CP-zhouqing')
# export_svn_log('https://svn.mdsd.cn:7443/svn/PreHospitalEmergency/trunk',
#                'CP-xuqiwei')

