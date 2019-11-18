import os
import sys
import glob
import fitz
import re
import numpy
from PIL import Image

def get_pdf_files(pdf_path):
    if pdf_path[len(pdf_path) - 1] != '\\':
        pdf_path = pdf_path + '\\'
    pdf_files = glob.glob(pdf_path+'*.pdf')
   
    return pdf_files

def pdf_to_imgs(pdf_files):
    pdf_imgs_full_path = []
    zoom = 200
    rotate = 0
    pdf_imgs = []
    pdf_img_path,dummy = os.path.split(pdf_files[0])
    pdf_img_path = pdf_img_path + '\\img\\'

    folder_exist = os.path.exists(pdf_img_path)
    if not folder_exist:
        os.makedirs(pdf_img_path)

    for pdf_file in pdf_files:
        pdf_doc = fitz.open(pdf_file)
        pdf_page = pdf_doc[0]
        pdf_trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pix_map = pdf_page.getPixmap(matrix = pdf_trans, alpha = False)

        dummy,pdf_file_name = os.path.split(pdf_file)
        pdf_img_full_path = pdf_img_path + re.sub('.[Pp][Dd][Ff]','_',pdf_file_name)+'.png'
        pdf_imgs_full_path.append(pdf_img_full_path)
        pix_map.writePNG(pdf_img_full_path)
        pdf_img = numpy.array(Image.open(pdf_img_full_path))
        pdf_imgs.append(pdf_img)
    
    return pdf_imgs,pdf_imgs_full_path

def cover_method(pdf_img, start_x, start_y, end_x, end_y, pdf_img_full_path):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            pdf_img[x, y] = 0
    pdf_img = Image.fromarray(pdf_img.astype("uint8"))
    pdf_img.save(pdf_img_full_path)


def img_cover(pdf_imgs,pdf_imgs_full_path):
    coordinate_config = open('coordinate.txt', 'r')
    start_x = []
    start_y = []
    end_x = []
    end_y = []

    for line in coordinate_config:
        points = line.split()
        start_x.append(points[0])
        start_y.append(points[1])
        end_x.append(points[2])
        end_y.append(points[3])
        
    for i in range(0, len(pdf_imgs)):
        for j in range(0, len(start_x)):
            cover_method(pdf_imgs[i],start_x[j],
                                     start_y[j],
                                     end_x[j],
                                     end_y[j],
                                     pdf_imgs_full_path[i])


if __name__ == '__main__':
    pdf_imgs = pdf_imgs_full_path = []
    pdf_path = input('Please input the PDF folder path:')
    if pdf_path == '':
        pdf_path = 'test666/' # default pdf path
        print('PDF path is:', pdf_path)
    pdf_files = get_pdf_files(pdf_path)
    pdf_imgs,pdf_imgs_full_path = pdf_to_imgs(pdf_files)
    img_cover(pdf_imgs,pdf_imgs_full_path)
