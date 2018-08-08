from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from .helper.extension_checker import allowed_file
from sklearn.externals import joblib
import json
import numpy as np
import pandas as pd


def LogisticRegressionController(request=None):
    user_name = request.form['user_name']
    model_name = request.form['model_name']

    if request.form['process']=='train':
        dataset = request.files['data']
        if not allowed_file(dataset.filename):
            return 'file not allowed'
        x_features = request.form['x_features']
        x_features = properify_str(x_features)
        y_features = request.form['y_features']
        test_size = float(request.form['test_size'])
        
        df = pd.read_csv(dataset)
        X_data = pd.DataFrame()
        for i in range(len(x_features)):
            X_data[x_features[i]] = df[x_features[i]]
        label = df[y_features]
        
        X_train, X_test, y_train, y_test = train_test_split(X_data, label, test_size=test_size, random_state=101)
        
        lr = LogisticRegression()
        lr.fit(X_train,y_train)
        joblib.dump(lr,'trained_models/'+'logistic_model'+user_name+model_name+'.pkl')
        return 'Ok model trained'
    
    x = request.form['x']
    x = properify_float(x)
    lr = joblib.load('trained_models/'+'logistic_model'+user_name+model_name+'.pkl')
    return " ".join(list(map(str,lr.predict(np.array(x).reshape(1,-1)))))

def properify_str(features):
    t = features.split(',')
    print(t)
    return t

def properify_float(features):
    t = features.split(',')
    t = list(map(float,t))
    print(t)
    return t
