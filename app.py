from flask import Flask,render_template

app = Flask(__name__)

app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

app.route('/predict')
def predict():
    try:
        return render_template('predict.html')
    except Exception as e:
        return str(e)