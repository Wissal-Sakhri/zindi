from flask import Flask, render_template,request
import numpy as np
import joblib

app = Flask(__name__)
#template_folder='templates
pickle_in=open("/random_model.pkl", 'rb')

model= joblib.load(pickle_in)




@app.route('/') #current page directory
def home():
    return render_template('home.html')



@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1]*100,0)
    return render_template('home.html', prediction_text=' {} % Of being victimized in the last 5 years '.format(output))
