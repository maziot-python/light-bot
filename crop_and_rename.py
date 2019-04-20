# -*- coding:utf-8 -*-
from PIL import Image
import os

path = './'
files = os.listdir(path)

start_string = input('请输入图片前缀:')
count = 0

for file_name in files:
    if file_name.endswith(".png"):
        original_image = Image.open(file_name)
        original_width, original_height = original_image.size

        # 仅第一次会做裁剪和增加背景动作
        if original_width == 2248:
            x1 = 135
            y1 = 0
            x2 = 2055
            y2 = 1080
            cropped_image = original_image.crop((x1, y1, x2, y2))
            cropped_image.save(file_name)

        count = count + 1

        if count == 1:
            new_file_name = '%stitle.png' % (start_string)
        elif count == 2:
            new_file_name = '%smenu.png' % (start_string)
        else:
            new_file_name = '%s%02d.png' % (start_string, count - 2)

        print(file_name, '>>>', new_file_name)
        os.rename(file_name, new_file_name)

print('done')