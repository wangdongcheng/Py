import os
import glob
import re
import fitz
import numpy
from PIL import Image
import img2pdf

# =========================================================
# get PDF files from given path
# =========================================================
def get_pdf_files(pdf_path):
    if pdf_path[len(pdf_path) - 1] != '/':
        pdf_path = pdf_path + '/'
    pdf_files = glob.glob(pdf_path+'*.pdf')
    return pdf_path, pdf_files

# =========================================================
# convert PDF to images
# =========================================================
def pdf_to_imgs(pdf_files):
    pdf_imgs_full_path = []
    ZOOM = 200
    ROTATE = 0
    pdf_imgs = []
    pdf_img_path, dummy = os.path.split(pdf_files[0])
    pdf_img_path = pdf_img_path + '/img/'

    if not os.path.exists(pdf_img_path):
        os.makedirs(pdf_img_path)

    for pdf_file in pdf_files:
        pdf_doc = fitz.open(pdf_file)
        dummy, pdf_file_name = os.path.split(pdf_file)
        for i in range(0, pdf_doc.pageCount):
            pdf_page = pdf_doc[i]
            pdf_trans = fitz.Matrix(ZOOM / 100.0, ZOOM / 100.0).preRotate(ROTATE)
            pix_map = pdf_page.getPixmap(matrix=pdf_trans, alpha=False)
            pdf_img_full_path = (pdf_img_path + re.sub('.[Pp][Dd][Ff]', '_', pdf_file_name) 
                                 + str(i).zfill(2) +'.png')
            pdf_imgs_full_path.append(pdf_img_full_path)
            pix_map.writePNG(pdf_img_full_path)
            pdf_img = numpy.array(Image.open(pdf_img_full_path))
            pdf_imgs.append(pdf_img)
    return pdf_imgs, pdf_imgs_full_path

# =========================================================
# add black block on the images
# =========================================================
def cover_method(pdf_img, start_x, start_y, end_x, end_y, pdf_img_full_path):
    for x_pos in range(int(start_x), int(end_x)+1):
        for y_pos in range(int(start_y), int(end_y)+1):
            pdf_img[y_pos, x_pos] = 0
    pdf_img = Image.fromarray(pdf_img.astype("uint8"))
    pdf_img.save(pdf_img_full_path)

# =========================================================
# proceed to add black block cover by given coordinates
# =========================================================
def img_cover(pdf_imgs, pdf_imgs_full_path):
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
            cover_method(pdf_imgs[i], start_x[j], start_y[j], 
                                      end_x[j], end_y[j],
                                      pdf_imgs_full_path[i])

def img_to_pdf(pdf_path, pdf_files):
    if pdf_path[len(pdf_path) - 1] != '/':
        pdf_path = pdf_path + '/'
    output_path = pdf_path + 'output/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    pdf_img_path = pdf_path + 'img/'
    for pdf_file in pdf_files:
        dummy, pdf_fullname = os.path.split(pdf_file)
        output_fullpath = output_path + pdf_fullname
        pdf_filename = pdf_fullname.split('.')[0]
        pdf_png_files = glob.glob(pdf_img_path + pdf_filename + '*.png')
        with open(output_fullpath,"wb") as f:
            f.write(img2pdf.convert(pdf_png_files))

# =========================================================
# Main
# =========================================================
def main():
    pdf_imgs = pdf_imgs_full_path = []
    pdf_path = input('Please input the PDF folder path:')
    if pdf_path == '':
        pdf_path = 'test666/' # default PDF path
        print('PDF path is:', pdf_path)
    pdf_path, pdf_files = get_pdf_files(pdf_path)
    pdf_imgs, pdf_imgs_full_path = pdf_to_imgs(pdf_files)
    img_cover(pdf_imgs,pdf_imgs_full_path)
    img_to_pdf(pdf_path,pdf_files)


if __name__ == '__main__':
    main()
