# coding:utf-8
# Excel操作模块

import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')  # 创建一个Excek模块
worksheet = workbook.add_worksheet()  # 创建一个工作表对象

worksheet.set_column('A:A', 20)  # 设定第一行(A)宽度为20像素
bold = workbook.add_format({'bold': True})  # 定义一个加粗格式的对象

worksheet.write('A1', 'Hello')  # A1单元格写入'hello'并引用加粗格式对象bold
worksheet.write('A2', 'World')  # A2单元格写入'World'并引用加粗格式对象bold
worksheet.write('B2', u'中文测试', bold)  # B2单元格写入中文并引入加粗格式对象bold

worksheet.write(2, 0, 32)  # 用行号表示写入数字’32‘与’35.5‘
worksheet.write(3, 0, 35.5)  # 行表示法的单元格下表--作为起始值，’3,0‘等价于A3
worksheet.write(4, 0, '=SUM(A3:A4)')  # 求A3:A4的和，并将结果写入 ’4,，0‘,即A5

# worksheet.insert_image('B5', 'img/python-logo.png')  # 在B5单元格插入图片
workbook.close()  #  关闭Excel文件
