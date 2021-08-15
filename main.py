from flask import Flask,render_template,request
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

app = Flask(__name__,template_folder='template')
pickle_in=open("model.pkl", 'rb')

model= joblib.load(pickle_in)


@app.route('/') #current page directory
def home():
    return render_template('home.html')



@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features=[x for x in request.form.values()]

    test = pd.read_csv("Test.csv")
    test = test.drop(['ID','gender','psu'], axis =1)
    test.iloc[0] = int_features

    le = LabelEncoder()
    test['race'] = le.fit_transform(test['race'])
    test['dwelling'] = le.fit_transform(test['dwelling'])
    test['dwelling_type'] = le.fit_transform(test['dwelling_type'])
    test['province_code'] = le.fit_transform(test['province_code'])
    test['metro_code'] = le.fit_transform(test['metro_code'])
    test['nationality'] = le.fit_transform(test['nationality'])
    test['RTH'] = le.fit_transform(test['RTH'])
    test['marital_st'] = le.fit_transform(test['marital_st'])
    test['Lang_inside'] = le.fit_transform(test['Lang_inside'])
    test['Lang_outside'] = le.fit_transform(test['Lang_outside'])
    test['Education'] = le.fit_transform(test['Education'])
    test['lw_work'] = le.fit_transform(test['lw_work'])
    test['lw_business'] = le.fit_transform(test['lw_business'])
    test['help_on_household'] = le.fit_transform(test['help_on_household'])
    test['job_or_business'] = le.fit_transform(test['job_or_business'])
    test['nature_of_work'] = le.fit_transform(test['nature_of_work'])

    stdscale = StandardScaler()
    test[["age"]] = stdscale.fit_transform(test[["age"]])

    print(int_features)
  
    prediction = model.predict_proba(test)[:,1]
    print(prediction[0])

    if prediction[0] < 0.5:
        final_output = "Low risk of being victimized"
    else:
        final_output = "High risk of being victimized"
    return render_template('home.html', prediction_text= final_output)
