# https://github.com/josch/img2pdf

import img2pdf

pdfpath = 'test666/out_2.pdf'
img1    = 'test666/Frontpage_1.png'
img2    = 'test666/Frontpage_2.png'
# multiple inputs (variant 1)
with open(pdfpath,"wb") as f:
	f.write(img2pdf.convert(img1, img2))

#import img2pdf

## opening from filename
#with open("name.pdf","wb") as f:
#	f.write(img2pdf.convert('test.jpg'))

## opening from file handle
#with open("name.pdf","wb") as f1, open("test.jpg") as f2:
#	f1.write(img2pdf.convert(f2))

## using in-memory image data
#with open("name.pdf","wb") as f:
#	f.write(img2pdf.convert("\x89PNG...")

## multiple inputs (variant 1)
#with open("name.pdf","wb") as f:
#	f.write(img2pdf.convert("test1.jpg", "test2.png"))

## multiple inputs (variant 2)
#with open("name.pdf","wb") as f:
#	f.write(img2pdf.convert(["test1.jpg", "test2.png"]))

## writing to file descriptor
#with open("name.pdf","wb") as f1, open("test.jpg") as f2:
#	img2pdf.convert(f2, outputstream=f1)

## specify paper size (A4)
#a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
#layout_fun = img2pdf.get_layout_fun(a4inpt)
#with open("name.pdf","wb") as f:
#	f.write(img2pdf.convert('test.jpg', layout_fun=layout_fun))