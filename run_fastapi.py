from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import nest_asyncio
import torch
import os

app = FastAPI()

# Check if CUDA (GPU) is available, otherwise default to CPU
device = 0 if torch.cuda.is_available() else -1

sentiment_analysis = pipeline("sentiment-analysis", model="malay-deberta-xsmall", device=device)

class TextRequest(BaseModel):
    text: str

@app.post("/predict/")
async def predict_sentiment(request: TextRequest):
    # Perform sentiment analysis on the text provided in the request
    result = sentiment_analysis(request.text)
    return {"sentiment": result}

if __name__ == '__main__':
    import uvicorn
    nest_asyncio.apply()
    CDSW_APP_PORT = os.getenv('CDSW_APP_PORT', 8100)
    uvicorn.run(app, host="127.0.0.1", port=int(CDSW_APP_PORT))
