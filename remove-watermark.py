from skimage import io
from pdf2image import convert_from_path
import numpy as np

import os
import img2pdf

'''
判断的参考代码：https://github.com/LJSthu/Python-Remove-Watermark/blob/master/watermark.py
img2pdf,环境：需先执行：`brew install poppler`
遍历当前目录下所有的jpg文件,并按照文件夹名称合并成pdf文档
'''

# change these paths to your own file path

# source pdf path
input_dir = '/Users/frank/Code/Python/from'
# target pdf path
output_dir = '/Users/frank/Code/Python/to'
# temp image dir path
img_dir = '/Users/frank/Code/Python/temp'


# 选择像素点(select pixel point)
def select_pixel(r, g, b):
    if 175 < r < 250 and 175 < g < 250 and 175 < b < 250:
        return True
    else:
        return False


# 处理图片矩阵(handle image matrix)
def handle(matrix):
    height = matrix.shape[0]
    width = matrix.shape[1]
    for i in range(height):
        for j in range(width):
            if select_pixel(matrix[i][j][0], matrix[i][j][1], matrix[i][j][2]):
                matrix[i][j] = (255, 255, 255)
                # matrix[i][j][0] = matrix[i][j][1] = matrix[i][j][2] = 255
    return matrix


# 将 pdf 文件转为 img 文件(convert pdf file to jpg file)
def convert_pdf_2_img(input_file):
    images = convert_from_path(input_file)
    index = 1
    img_length = len(images)
    print(os.path.basename(input_file), 'is converted to : ', img_length, ' images')
    for img in images:
        img = np.array(img)
        img = handle(img)
        io.imsave(img_dir + '/' + str(index) + '.jpg', img)
        print(index, '/', img_length)
        index += 1


# 将 img 文件合并为 pdf(convert img files to pdf file)
def image2pdf(img_path, output_path):
    list_of_img_name = sorted(os.listdir(img_path), key=lambda x: int(x[:-4]))
    list_of_img_path = []
    for file_path in list_of_img_name:
        if file_path.endswith(".jpg"):
            list_of_img_path.append(os.path.join(img_path, file_path))
        else:
            pass

    with open(output_path + ".pdf", "wb+") as f:
        f.write(img2pdf.convert(list_of_img_path))
    print(output_path + '.pdf is done.')


# 删除目录 _dir 下的所有文件(delete files under the _dir)
def remove_file_in_dir(_dir):
    print('start to delete temp files under the ', _dir, ' ...', end=' ')
    for _file in os.listdir(_dir):
        if _file[-4:] == '.jpg':
            os.remove(os.path.join(_dir, _file))
    print('all temp jpg files are deleted!')


# main function
if __name__ == '__main__':
    for file in os.listdir(input_dir):
        if file[-4:] == '.pdf':
            name = os.path.splitext(file)[0]
            convert_pdf_2_img(os.path.join(input_dir, file))
            print('start to merge jpg files to pdf ...')
            image2pdf(img_dir, os.path.join(output_dir, name))
            remove_file_in_dir(img_dir)
