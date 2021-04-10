from flask import Flask, request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('household_power_consumption.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    """
    For rendering results on HTML GUI
    """
    x_test = [[float(x) for x in request.form.values()]]
    if(x_test[0][0] == 0):
        x_test[0][0] = 0
        x_test[0].insert(1,0)
    elif(x_test[0][0] == 1):
        x_test[0][0] = 1
        x_test[0].insert(1,0)
    else:
        x_test[0][0] = 0
        x_test[0].insert(1,1)
        
    prediction = model.predict(x_test)
    output = prediction[0]
    
    return render_template('index.html', prediction_text="Power: {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
    