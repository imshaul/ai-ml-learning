class PDFfile:
    def open(self):
        print("PDF opened")
class ImageFile:
    def open(self):
        print("Image opened")

class VideoFile:
    def open(self):
        print("Video opened")

def open_file(file):
    file.open()

pdf=PDFfile()
img=ImageFile()
vid=VideoFile()

open_file(pdf)
open_file(img)
open_file(vid)


