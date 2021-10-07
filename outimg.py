from PIL import Image
import cv2
import numpy
import os

def colour(c1,c2,c3): #组合数据函数
    return round(c1),round(c2),round(c3)

def out_rgb(filname):
    try:
        myimg_blur = cv2.imread(filname) #读取图片

        size = (128,128) 

        myimg_blur_ys = cv2.resize(myimg_blur, size, interpolation=cv2.INTER_AREA) #压缩图片快速处理 免得服务器带不动((

        bblur = cv2.GaussianBlur(myimg_blur_ys, (2555,2555), 5)#进行高斯模糊处理

        cv2.imwrite('./tmp/dimg_blur.png', bblur)

        myimg = cv2.imread('./tmp/dimg_blur.png')

        os.remove('./tmp/dimg_blur.png')

        avg_color_per_row = numpy.average(myimg, axis=0)

        avg_color = numpy.average(avg_color_per_row, axis=0) #进行图片颜色平均值

        img_obj = Image.new('RGB', (800, 480), colour(avg_color[2],avg_color[1],avg_color[0]))  

        with open('./out_rgb/dimg.png','wb') as f:
                img_obj.save(f,'png')

        return True
    except Exception as rrr:
        print(rrr)
        return False
