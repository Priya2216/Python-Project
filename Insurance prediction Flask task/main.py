from flask import Flask, render_template, request
import pickle
import numpy as np 

app = Flask(__name__)

file=open("model.pkl","rb")
model=pickle.load(file)
file.close()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        #access the data from form
        
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        children = int(request.form["children"])
        Sex = int(request.form["Sex"])
        Smoker = int(request.form["Smoker"])
        Region = int(request.form["Region"])
        Charges= int(request.form["Charges"])
    
        # prediction
    
        output= model.predict(np.array([age, bmi, children, Sex, Smoker, Region,Charges]).reshape(1,-1))
        
        if output[0] == 1:
             return('You are claim for insurance')
        else:
             return("No claim for insurance")
        
        return render_template("index.html", prediction_text= "output")

       
if __name__ == "__main__":
    app.run(debug=True)