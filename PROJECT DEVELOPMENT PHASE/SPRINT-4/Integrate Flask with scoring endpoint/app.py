import os
import pickle

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

model=joblib.load('model.pkl')

app=Flask(__name__)
@app.route('/')
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/y_predict",methods=['POST'])
def predict():
    name=request.form['name']

    month=request.form['Month']
    dayofmonth=request.form['dayofmonth']
    dayofweek=request.form['dayofweek']
    origin=request.form['origin']
    if(origin=="delhi"):
        origin = 1
    if(origin=="chennai"):
        origin= 10000
    if(origin=="mumbai"):
        origin= 100
    if(origin=="bangalore"):
        origin=1000
    if(origin=="hyderabad"):
        origin=11

    destination=request.form['destination']
    if(destination=="chennai"):
        destination=1000
    if(destination=="mumbai"):
        destination=1
    if(destination=="delhi"):
        destination=11
    if(destination=="bangalore"):
        destination=100
    if(destination=="hyderabad"):
        destination=10

    dept=request.form['dept']
    arrtime=request.form['arrtime']
    actdept=request.form['actdept']
    # dept15=int(dept)-int(actdept)
    total=[[name,month,dayofmonth,dayofweek,origin,destination,arrtime,dept,actdept]]
    y_pred=model.predict(total)
    if(y_pred==0):
        return render_template("delayed.html")
    else:
        return render_template("ontime.html")
if __name__=='__main__':
    app.run()