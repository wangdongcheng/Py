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
        pix_map.writePNG(pdf_img_full_path)
        pdf_img = numpy.array(Image.open(pdf_img_full_path))
        list.append(pdf_imgs,pdf_img)
    
    return pdf_imgs

if __name__ == '__main__':
    pdf_path = input('Please input the PDF folder path:')
    pdf_files = get_pdf_files(pdf_path)
    pdf_imgs = pdf_to_imgs(pdf_files)
