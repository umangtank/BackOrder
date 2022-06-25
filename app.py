from flask import Flask,render_template,request,json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            # return render_template('predict.html')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)