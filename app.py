import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('prediction.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('login.html')
database={'admin':'123','test':'123','demo':'123'}

@app.route('/login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('predict.html',name=name1)


@app.route('/home',methods=['GET','POST'])
def index():
    return render_template("index.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
    
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template('predict.html', prediction_text='Volume weighted average price $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)