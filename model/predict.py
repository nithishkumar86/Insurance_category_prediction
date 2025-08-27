import pickle
import pandas as pd


with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

MODEL_VERSION='1.0.0'

class_labels=model.classes_.tolist()


def input_predict(input:dict):

    df=pd.DataFrame([input])

    predicted_class=model.predict(df)[0]

    probabilities=model.predict_proba(df)[0]
    confidence=max(probabilities)

    class_probs=dict(zip(class_labels,map(lambda x : round(x,2),probabilities)))

    return {
        "predicted_category":predicted_class,
        "confidence":round(confidence,2),
        "class_probabilities":class_probs
    }
