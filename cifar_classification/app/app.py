from flask import Flask, render_template, request, jsonify, redirect
import base64
import numpy as np
import pickle as pkl
import cv2
import os
from predict import predict_image
app = Flask(__name__)
stats = None

if not os.path.exists('stats/stats.pkl'):
    stats = { 'yes':0, 'no':0 }
    with open('stats/stats.pkl', 'wb') as fp:
        pkl.dump(stats,fp)

def accuracy():
    acc = '100'
    with open('stats/stats.pkl', 'rb') as fp:
        global stats;
        stats = pkl.load(fp)
        total = sum(stats.values())
        if total!=0: acc = f"{ 100*stats['yes']/total:.2f} ({stats['yes']}/{total})"
    return acc


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		image=request.files['image']
		image_string = base64.b64encode(image.read());print(image_string);
		binary = base64.b64decode(image_string)
		img = np.asarray(bytearray(binary), dtype="uint8")
		img = cv2.imdecode(img, 1)
		img = cv2.resize( img, (32,32), interpolation=cv2.INTER_AREA );pred = predict_image(img.reshape(1,32,32,3));
		return render_template('index.html', data={ 'status':True, 'img': str(image_string)[2:-1], 'pred': pred, 'accuracy':accuracy()})
	else:
		return render_template('index.html', data={ 'status':False, 'accuracy':accuracy() })


@app.route('/no', methods=['get'])
def no():
    with open('stats/stats.pkl', 'wb') as fp:
        stats['no']+=1
        pkl.dump(stats,fp)
    return redirect('/')

@app.route('/yes', methods=['get'])
def yes():
    with open('stats/stats.pkl', 'wb') as fp:
        stats['yes']+=1
        pkl.dump(stats,fp)
    return redirect('/')

if __name__=='__main__':
    app.run(host = '0.0.0.0',port = int(80))
