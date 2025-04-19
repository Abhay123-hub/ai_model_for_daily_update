from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from workflow import workflow
import pickle
from typing import Dict, Any

app = FastAPI()




class InputData(BaseModel):
    data: list




@app.post("/predict")
async def predict(input_data:InputData):
    try:
        # Step 1: Convert JSON to DataFrame
       graph = workflow()
       input = input_data.data[0]

       response = graph.execute(input)

       

        # Step 3: Make predictions using the model
       

        # Step 4: Return the predictions as JSON
       return {"predictions": response}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))