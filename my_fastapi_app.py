from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class InputData(BaseModel):
    # Define the structure of input data
    feature1: float
    feature2: float

@app.post("/predict/")
def predict(data: InputData):
    # Load your pre-trained model
    model = joblib.load(r"C:\Users\dell\Documents\AJAX-Movie-Recommendation\movies_metadata.csv")
    # Make predictions
    prediction = model.predict([[data.feature1, data.feature2]])
    return {"prediction": prediction.tolist()}
