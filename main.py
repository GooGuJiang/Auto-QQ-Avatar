import os
from flask import Flask,redirect
from flask import abort
import outimg as o
import requests
from flask import make_response
import md55 # 文件检测
import yaml

def qqset():
    with open('settings.yml', 'r') as f: #读取配置文件?
        qq = yaml.load(f.read(),Loader=yaml.FullLoader)
        token = qq['QQnum']
    return token

app = Flask(__name__)
@app.route('/')
def index():
    return redirect('https://gmoe.cc', code=302)

@app.route('/rgb')
def rggbb_img():

    durl = "https://q1.qlogo.cn/g?b=qq&nk="+str(qqset())+"&s=640"
    if os.path.isfile('./tmp/dimg.png') == True:
        dwimg = requests.get(durl)
        
        with open("./tmp/dimg_tmp.png","wb")as f: #下载图片
            f.write(dwimg.content)
        
        if md55.diff_md5('./tmp/dimg_tmp.png','./out_rgb/dimg.png') == False: #如果文件MD5不一样就重新生成
            if o.out_rgb("./tmp/dimg_tmp.png") == False: #检测图片生成时候出错
                return abort(400, '淦!生成图片时候出错了') 
            else:
                os.remove("./tmp/dimg.png")
                os.rename("./tmp/dimg_tmp.png", "./tmp/dimg.png")   
                image_data = open("./out_rgb/dimg.png", "rb").read()#读取图片
                response = make_response(image_data)
                response.headers['Content-Type'] = 'image/jpg'
                return response
        else:
            os.remove("./tmp/dimg_tmp.png")
            image_data = open("./out_rgb/dimg.png", "rb").read()#读取图片
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response

    else:
        dwimg = requests.get(durl)
        with open("./tmp/dimg.png","wb")as f: #下载图片
            f.write(dwimg.content)

        if o.out_rgb("./tmp/dimg_tmp.png") == False: #检测图片生成时候出错
            return abort(400, '淦生成图片时候出错了') 
        else:    
            image_data = open("./out_rgb/dimg.png", "rb").read()#读取图片
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'

            return response

@app.route('/img')
def qq_img():
    durl = "https://q1.qlogo.cn/g?b=qq&nk="+str(qqset())+"&s=640"
    if os.path.isfile('./qqimg/dimg.png') == True:
        dwimg = requests.get(durl)
        
        with open("./qqimg/qq_tmp.png","wb")as f: #下载图片
            f.write(dwimg.content)
        
        if md55.diff_md5('./qqimg/qq_tmp.png','./qqimg/qq.png') == False: #如果文件MD5不一样就重新下载
            os.remove("./qqimg/qq.png")
            os.rename("./qqimg/qq_tmp.png", "./qqimg/qq.png")   
            image_data = open("./qqimg/qq.png", "rb").read()#读取图片
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response
        else:
            os.remove("./qqimg/qq_tmp.png")
            image_data = open("./qqimg/qq.png", "rb").read()#读取图片
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response

    else:
        dwimg = requests.get(durl)
        with open("./qqimg/qq.png","wb")as f: #下载图片
            f.write(dwimg.content)

        image_data = open("./qqimg/qq.png", "rb").read()#读取图片
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int("10086"))