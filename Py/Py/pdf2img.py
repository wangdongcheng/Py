import fitz
import glob
import os
import sys
import re

def rightinput(desc):
    flag=True
    while(flag):
        instr = input(desc)
        try:
            intnum = eval(instr)
            if type(intnum)==int:
                flag = False
        except:
            print('请输入正整数！')
            pass
    return intnum

pdffile = glob.glob("test666/a9ba298_36471.pdf")[0]
doc = fitz.open(pdffile)


flag = rightinput("输入：1：全部页面；2：选择页面\t")
if flag == 1:
    start = 0
    totaling = doc.pageCount
else:
    start = rightinput('输入起始页面：') - 1
    totaling = rightinput('输入结束页面：') 

for pg in range(start, totaling):
    page = doc[pg]
    zoom = int(200)
    rotate = int(0)
    trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    # pm.writePNG('d:/My Documents/BaiduCloud/SICOD/GitHub/Py/test/%s.png' % str(pg+1))
    imgname = re.sub('.[Pp][Dd][Ff]','_',pdffile)
    pm.writePNG(imgname+str(pg+1)+'.png')