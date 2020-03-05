#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, session
from sklearn import svm
from PIL import Image
from joblib import dump, load
import csv

DATA_PATH = 'nums.csv'
RETRAIN_RATE = 10

app = Flask(__name__)
app.secret_key = 'blahblahblah'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/ml')
def ml():
    session['ml'] = True
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        pixels_str = request.form['pixels']
        pixels = pixels_str.split(',')

        session['pixels'] = pixels

        indicator = int(open('build_indicator.txt', 'r').read())
        print(indicator)

        # grab saved model
        if indicator > 0:
            print('using saved model')
            clf = load('clf.model')

        # build the SVM model
        else:
            print('building new model')
            data = []
            with open(DATA_PATH) as f:
                reader = csv.reader(f)
                for r in reader:
                    data.append(r)

            labels, values = [], []

            for row in data:
                labels.append(int(row[0]))
                
                vals = row[1:]
                vals_ints = [int(x) for x in vals]
                
                values.append(vals_ints)

            clf = svm.SVC(kernel='linear') 
            clf = clf.fit(values, labels)

            dump(clf, 'clf.model')
            with open('build_indicator.txt', 'w') as f:
                f.write(f'{RETRAIN_RATE}')

        pred = clf.predict([pixels])
        pred = int(tuple(pred)[0])

        ml = session.get('ml', False)

        return render_template('result.html', pred=pred, ml=ml)
    
    except:
        return render_template('error.html')

@app.route('/update', methods=['POST'])
def update():

    ans = request.form['yesno']

    if ans == 'yes':
        ins_num = int(request.form['pred_num'])
    else:
        ins_num = int(request.form['real_num'])

    if ins_num is None:
        print("none")
    
    if ins_num is None or ins_num not in (0,1,2,3,4,5,6,7,8,9):
        return render_template('error.html')

    pixels = session['pixels']
    pixels.insert(0, ins_num)    

    pixels = [pixels]

    with open(DATA_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(pixels)   

    indicator = int(open('build_indicator.txt', 'r').read())
    with open('build_indicator.txt', 'w') as f:
        f.write(f'{indicator-1}')

    return render_template('index.html')

#
#   use when starting from scratch.
#   just change the <form> action 
#   from "/predict" to "/addNew"
# 
# @app.route('/addNew', methods=['POST'])
# def add_new():
    
#     num = request.form['num']
    
#     pixels_str = request.form['pixels']
#     pixels = pixels_str.split(',')

#     pixels.insert(0, num)

#     pixels = [pixels]

#     with open(DATA_PATH, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(pixels)

#     return render_template('index.html')

if __name__ == '__main__':
    app.run()