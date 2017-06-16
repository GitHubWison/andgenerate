# coding=utf-8
import generate_tools
import os

input_name = "ifly_test"
mod_array = input_name.split("_")
# 获得模块名称，如＂TestAnd＂
module_name = '%s%s%s%s' % (mod_array[0][:1].upper(), mod_array[0][1:], mod_array[1][:1].upper(), mod_array[1][1:])
# 获得文件名，如＂testand＂
project_name = '%s%s' % (mod_array[0], mod_array[1])
# 资源文件名，如＇test_andv2＇
layout_name = input_name
# 变量名
var_name = '%s%s%s' % (mod_array[0], mod_array[1][:1].upper(), mod_array[1][1:])
# projectpath
project_path = '%s%s%s%s' % (
    generate_tools.output_path, generate_tools.seplator, project_name, generate_tools.seplator)
# views
views_path = '%s%s' % (project_path, 'views/')
# viewmodels
viewmodels_path = '%s%s' % (project_path, 'viewmodels/')
# childs_views
childs_views_path = '%s%s' % (project_path, 'childs/views/')
# childs_viewmodels
childs_viewmodels_path = '%s%s' % (project_path, 'childs/viewmodels/')
# 各种接口的路径
interface_path = '%s%s' % (project_path, 'iviews/')
# 子项目中各种接口的路径
childs_interface_path = '%s%s' % (project_path, 'childs/iviews')
# 资源文件,布局文件等
res_layout_path = '%s%s' % (project_path, 'layoutfiles/')


# 创建各种文件夹
def make_flodders():
    print '创建文件夹'
    generate_tools.make_dir(views_path)
    generate_tools.make_dir(viewmodels_path)
    generate_tools.make_dir(interface_path)
    generate_tools.make_dir(childs_viewmodels_path)
    generate_tools.make_dir(childs_views_path)
    generate_tools.make_dir(childs_interface_path)
    generate_tools.make_dir(res_layout_path)


# 创建android文件
# template_name:模块名称，通常放在template目录下面
# module_replace_name_dic:模板中需要替换的替身如：>>>xxx<<<
# file_type_name:生成文件的后缀名和文件类型如：Fragment.java
def make_android_files(views_path_name, template_name, module_replace_name_dic, file_type_name):
    print '创建android文件'
    os.system('pwd')
    generate_tools.make_outputfile(generate_tools.replace_keywords(
        generate_tools.read_template(template_name),
        module_replace_name_dic),
        '%s%s' % (views_path_name, file_type_name))


def make_muti_android_files():
    # 创建fragment文件s
    make_android_files(views_path,
                       'fragment_template',
                       {
                           'module_name': module_name
                       },
                       '%s%s' % (module_name, 'Fragment.java'))
    # 创建actvity文件
    make_android_files(views_path,
                       'activity_template',
                       {'module_name': module_name,
                        'layout_name': layout_name,
                        'var_name': var_name}
                       , '%s%s' % (module_name, 'Activity.java'))
    # 创建activity_layout文件
    make_android_files(res_layout_path,
                       'activity_layout_template',
                       {'layout_name': layout_name,
                        'module_name': module_name},
                       '%s%s%s' % ('activity_', layout_name, '.xml'))
    # 创建fragment_layout文件
    make_android_files(res_layout_path,
                       'fragment_layout_template',
                       {
                           'module_name': module_name
                       },
                       '%s%s%s' % ('fragment_', layout_name, '.xml'))
    # 创建activity的接口文件
    make_android_files(interface_path,
                       'iviews_activity_template',
                       {
                           'module_name': module_name
                       },
                       '%s%s%s' % ('I', module_name, 'ActivityView.java'))
    # 创建fragment的接口文件
    make_android_files(interface_path,
                       'iviews_fragment_template',
                       {
                           'module_name': module_name,
                           'current_time': generate_tools.get_current_time()
                       },
                       '%s%s%s' % ('I', module_name, 'FragmentView.java'))
#     创建viewmodel文件
#     make_android_files(viewmodels_path)


# 创建文件夹
make_flodders()
make_muti_android_files()
