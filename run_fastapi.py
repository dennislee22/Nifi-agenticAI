from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import nest_asyncio
import torch
import os

# Create a FastAPI app
app = FastAPI()

# Check if CUDA (GPU) is available, otherwise default to CPU
device = 0 if torch.cuda.is_available() else -1

# Load the sentiment analysis model into memory when the app starts
sentiment_analysis = pipeline("sentiment-analysis", model="malay-deberta-xsmall", device=device)

# Define request body using Pydantic models
class TextRequest(BaseModel):
    text: str

# Define a POST endpoint for sentiment analysis
@app.post("/predict/")
async def predict_sentiment(request: TextRequest):
    # Perform sentiment analysis on the text provided in the request
    result = sentiment_analysis(request.text)
    return {"sentiment": result}

# If the script is run directly, use Uvicorn to serve the FastAPI app
if __name__ == '__main__':
    import uvicorn
    # Set the port for the server (default 8100)
    nest_asyncio.apply()
    CDSW_APP_PORT = os.getenv('CDSW_APP_PORT', 8100)
    uvicorn.run(app, host="127.0.0.1", port=int(CDSW_APP_PORT))
