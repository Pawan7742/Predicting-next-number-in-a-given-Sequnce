from flask import Flask,render_template,request
import numpy as np
from keras.models import load_model


app=Flask(__name__)


def clearString(text):
    text=text.split(" ")
    s=""
    for i in range(len(text)):
        s=s+text[i]
    
    s=s.split(",")
    return s



model=load_model('model/models1.h5')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods=["POST"])
def SubmitQuery():
    text=request.form['inp']
    li=[]
    s=clearString(text)
    for i in range(len(s)):
        x=int(s[i])
        li.append(x)
    li=np.array(li).reshape((1,5))
    
    preic=model.predict(li)
    preic=preic.round()
    return render_template("index.html",data=preic[0][0])

# @app.route('/prediction',methods=["GET"])
# def prediction():
#     return "Welcome to prediction"

if __name__ == "__main__":
    app.run(debug=True)