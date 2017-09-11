from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)

"""
The Django template language
原來 html 中的 {} 是變數，

這個整體 的html 叫， template language.

In this example, the {% block %} tags define four blocks that child templates can fill in. All the block tag does is tell the template engine that a child template may override those portions of the template.

Reference:
http://flask.pocoo.org/docs/0.12/patterns/templateinheritance/

這是把出一個獨立的環境
python -m venv virtual

-m 是把後 面的module 當成執行檔在執行 ， 後面的xxx ，是指令，

對於那個module 要下的指令, 像這個範例，就 是在當目録下，

拉出一個獨立的環境，東西放在virtual , 像你一班執 行 的python  pip ,

都會被放到這裡，  如果想在這獨 立的環境安裝 東西， 執 行 pip ，

也要用這個folder裡面的才行, 像virtual\scripts\python.


難怪之前有一個指令是  python -m flask run

t 

"""
