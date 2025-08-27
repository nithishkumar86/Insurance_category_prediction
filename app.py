from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import input_predict,model,MODEL_VERSION
from schema.user_input import InputBody
from schema.response import ResponseBody

app=FastAPI()

@app.get('/home')
def home_page():
    return {"message":"Insurance_premium_category"}


@app.get('/check')
def machine_purpose():
    return {
        'status':'ok',
        'version':MODEL_VERSION,
        'model':model is not None
    }


@app.post('/predict',response_model=ResponseBody)
def predict_model(input: InputBody):
    user_data= {
            "income_lpa": input.income_lpa,
            "occupation": input.occupation,
            "bmi": input.bmi,
            "age_group": input.age_group,
            "lifestyle_risk": input.lifestyle_risk
    }
    try:
        prediction=input_predict(user_data)
        return JSONResponse(status_code=200,content={"prediction": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


