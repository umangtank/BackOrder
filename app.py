from flask import Flask,render_template,request
import Training.Training_file as train
import Prediction.prediction as pred
import Data_ingestion.data_loder as data_loder

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/predict',methods=['GET','POST'])
def predict():
    # print('inside predict')
    if request.method == 'POST':
        try:
            sales_1_month = float(request.form['sales_1_month'])
            sales_3_month = float(request.form['sales_3_month'])
            sales_6_month = float(request.form['sales_6_month'])
            sales_9_month = float(request.form['sales_9_month'])
            forecast_3_month = float(request.form['forecast_3_month'])
            forecast_6_month = float(request.form['forecast_6_month'])
            forecast_9_month = float(request.form['forecast_9_month'])
            perf_6_month_avg = float(request.form['perf_6_month_avg'])
            perf_12_month_avg = float(request.form['perf_12_month_avg'])
    
            print(sales_1_month,sales_3_month,sales_6_month,sales_9_month,forecast_3_month,forecast_6_month,forecast_9_month,perf_6_month_avg,perf_12_month_avg)
            p = pred.prediction() #Predict A File
            data = p.convert_input_into_data([forecast_3_month,forecast_6_month,forecast_9_month,sales_1_month,sales_3_month,sales_6_month,sales_9_month,perf_6_month_avg,perf_12_month_avg])
            # print(data)
            p.get_prediction(data)

            predict = data_loder.dataGatter()
            print(predict)
            prediction = predict.prediction()
    
            # showing the prediction results in a UI
            if(list(prediction["Prediction"])[0] == 'No'):
                return render_template('predict.html', prediction = 0)
            else:
                return render_template('predict.html', prediction= 1)

        except Exception as e:
            print('The Exception message is:' , e)
            return 'something is wrong'


    else:
        return render_template('predict.html')

@app.route('/train',methods=['GET','POST'])
def training():
    print('inside train')
    train_obj = train.training()
    train_obj.trainingModel()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)