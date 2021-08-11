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
    final_features = [np.array(x_text)]
        
    prediction = model.predict(final_features)
    output = prediction[0]
    
    return render_template('index.html', prediction_text="Power consumed: {} kWh".format(output))


if __name__ == "__main__":
    app.run(debug=True)
    
