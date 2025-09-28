from fastapi import FastAPI,HTTPException,Path
import json
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model


app=FastAPI()


@app.get('/health')
def health():
    return {'status':'ok',
             'model_version' :'1.0.0',
             'model_loaded' : model is True
             }
@app.post('/predict') 
def predict(data:UserInput):
    user_input={
        'bmi':data.bmi,
        'city_tier':data.city_tier,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation,}

    prediction = predict_output(user_input)
    return JSONResponse(status_code=200,content={'prediction':prediction})
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

