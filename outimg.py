from PIL import Image
import cv2
import numpy

def colour(c1,c2,c3): #组合数据函数
    return round(c1),round(c2),round(c3)

def out_rgb(filname):
    try:
        myimg = cv2.imread(filname) #读取图片
        avg_color_per_row = numpy.average(myimg, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        img_obj = Image.new('RGB', (800, 480), colour(avg_color[2],avg_color[1],avg_color[0]))  
            #先将图片保存起来
        with open('./out_rgb/dimg.png','wb') as f:
                img_obj.save(f,'png')
        return True
    except Exception as rrr:
        print(rrr)
        return False

