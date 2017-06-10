# coding=utf-8
import os
import time

# 替代模板中的字符串
replace_start_str = '>>>'
replace_end_str = '<<<'
template_path = 'template'
seplator = '/'
# 模板文件格式
template_formate = ''
output_path = 'output'


# 将模板中需要替换的内容替换成ｄｉｃ中的内容
def replace_keywords(original_str, replace_dic):
    replace_str = '%s%s' % (original_str, '')
    for key in replace_dic:
        value = replace_dic[key]
        replace_str = replace_str.replace(make_replace_str(key), value)
    return replace_str


# 读取模板，返回模板字符串
def read_template(file_name):
    with open('%s%s%s%s' % (template_path, seplator, file_name, template_formate), 'r') as file_object:
        content = file_object.read()
        file_object.close()
    return content


# 制造模板中的需要替换的字符，如：>>>replace_1<<<
def make_replace_str(main_str):
    return '%s%s%s' % (replace_start_str, main_str, replace_end_str)


# 将字符串输出成文件,放到ｏｕｔｐｕｔ中
def make_outputfile(output_str, outputfile_path):
    with open(outputfile_path, 'w+') as file_object:
        file_object.write(output_str)
        file_object.close()


def make_dir(path):
    print path
    try:
        os.makedirs(r'%s' % path)
    except OSError:
        print '%s' % OSError.message


def get_current_time():
    return time.strftime('%Y年%m月%d日', time.localtime(time.time()))


# 打包文件
def tar_file(foldder_path, tar_name):
    shell = '%s%s%s%s' % ('tar -cvf ', tar_name, '.tar ', foldder_path)
    print shell
    os.system(shell)
    print '打包完成'

# tar_file('output/testandv2', 'test')
