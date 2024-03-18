from flask import Flask, render_template, request, jsonify,make_response,url_for,redirect
import json
import threading
import time

host=input('host:')
port=int(input('port:'))
def clear(timeforl):
    while True:
        time.sleep(timeforl)
        with open('almsg.txt','w',encoding='utf-8') as fp:
            fp.write('<p>start</p>')
        
clears= threading.Thread(target=clear,args=(1145,))
clears.start()


#创建Flask对象app并初始化
app = Flask(__name__)

@app.route("/")
def root():
    tunnel=0
    cookies=request.cookies
    if cookies:
        with open('user.json','r',encoding='utf-8') as fp:
            files=json.load(fp)
            for file in files:
                if cookies['ids'] == file:
                    tunnel=1
                    break
    
    if tunnel==0:
        return redirect(url_for('login'))
    else:
        return render_template('chating.html',ids=cookies['ids'])
    
#通过python装饰器的方法定义路由地址
@app.route("/login")
#定义方法 用jinjia2引擎来渲染页面，并返回一个index.html页面
def login():
    return render_template("index.html")

@app.route('/sendmsg',methods=['POST'])
def sendmsg():
    msg=request.form.get("msg")
    with open('almsg.txt','a',encoding='utf-8') as f:
        f.write(msg)
    with open('almsg.txt','r',encoding='utf-8') as f:
        remsg=f.read()
        resp=make_response({'statu':'success','remsg':remsg})
        return resp
    



#app的路由地址"/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交
@app.route("/submit",methods=["GET", "POST"])
#从这里定义具体的函数 返回值均为json格式
def submit():
    #由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    if request.method == "POST":
        ids = request.form.get("ids")
        pwds = request.form.get("pwds")
    if request.method == "GET":
        ids = request.args.get("ids")
        pwds = request.args.get("pwds")
    #如果获取的数据为空
    if len(ids) == 0 or len(pwds) ==0:
        return {'message':"error!"}
    else:
        with open('user.json','r',encoding='utf-8') as fp:
            file=json.load(fp)
            if file[ids]==pwds:
                resp=make_response({'message':"success!",'ids':ids,'pwds':pwds})
                resp.set_cookie('ids',ids)
                return resp
            else:
                return {'message':'error!'}
#定义app在端口运行
app.run(host=host,port=port)
