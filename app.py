from flask import Flask,render_template,request
import Training_file as train

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('predict.html')

@app.route('/train',methods=['GET','POST'])
def training():
    train_obj = train.training()
    train_obj.trainingModel()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)