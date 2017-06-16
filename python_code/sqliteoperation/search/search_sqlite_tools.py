# coding=utf-8
import sqlite3
import os
#数据库查询工具
db_path = '/sdcard/com.test.medicalsystem.medicalsystem/sqlite/wisdomaid.db'


def search(tb_name):
    conn = sqlite3.connect('wisdomaid.db')
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
    table_name_list = cursor.fetchall()
    # for table_name in table_name_list:
    #     print table_name[1]
    # cursor.execute("SELECT * FROM TB_Patient")
    cursor.execute("PRAGMA table_info(%s)" % tb_name)
    table_column_names = cursor.fetchall()
    table_values = cursor.execute("SELECT * FROM %s" % tb_name).fetchall()
    # print table_values
    content = ''
    columns = []
    values = []
    for table_column_name in table_column_names:
        # content = '%s%s%s' % (content, table_column_name[1], '\t')
        columns.append(table_column_name[1])
    content = '%s\n' % content
    for table_value in table_values:
        single_values = []
        for item_value in table_value:
            # content = '%s%s%s' % (content, item_value, '\t')
            single_values.append(item_value)
        # content = '%s\n' % content
        values.append(single_values)
    retdic = {'col': columns, 'val': values}
    return retdic


#     刷新数据库
def download_db():
    os.system('adb pull %s' % db_path)


# download_db()
# search('asd')
