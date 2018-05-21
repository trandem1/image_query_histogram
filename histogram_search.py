import cv2
import numpy as np
import glob
import operator

from builtins import int


def histogram_color_image(imgpath,bin):
    img = cv2.imread(imgpath)
    hist0 = cv2.calcHist([img], [0], None, [bin], [0, 255])
    hist1 = cv2.calcHist([img], [1], None, [bin], [0, 255])
    hist2 = cv2.calcHist([img], [2], None, [bin], [0, 255])
    hist = []
    for x in hist1:
        hist.append(x[0])
    for x in hist0:
        hist.append(x[0])
    for x in hist2:
        hist.append(x[0])
    histarr = np.asanyarray(hist)
    return histarr

def query_image_histogram(imgpaht,bin,kq):
    f1 =open('64_bin','r')
    imagediction = dict()
    hisquery = histogram_color_image(imgpaht, bin)
    for line in f1.readlines():
        linearr = line.split("\t")
        imagname = linearr[0]
        hist = []
        for item in linearr[1].split(" "):
            hist.append(float(str(item)))
        kq1 = np.linalg.norm(hist - hisquery)
        imagediction[imagname] = kq1
    sorted_x = sorted(imagediction.items(), key=operator.itemgetter(1))
    dem =0
    while dem < kq :
        dem = dem +1
        print(sorted_x[dem][0])
    return sorted_x

def store_image_histogram(filename,bin):
    f1 = open(filename,'w');
    for f in glob.iglob("image.orig/*"):
        his_image = histogram_color_image(str(f),bin)
        x =""
        for i in range(len(his_image)):
            x += str(his_image[i]) +" "
        f1.write(str(f) +"\t" + str(x.strip()))
        f1.write("\n")
    f1.close()


# store_image_histogram('256_bin',256)

"""
3 tham so co the chinh sua duoc trong method query_image_histogram 
lan luot la 
1: anh can tim kiem
2: so bin mau
3: so ket qua tra ve
"""
query_image_histogram('image.orig/178.jpg',64,10)

