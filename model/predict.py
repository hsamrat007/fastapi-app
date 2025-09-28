import pickle
import pandas as pd
import os # Import the os module

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

with open(model_path,'rb') as f:
    model=pickle.load(f)

def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    prediction =model.predict(input_df)[0]
    return prediction