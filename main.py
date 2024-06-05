from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/wordcount")
async def word_count(text: str = ""):
    # Calculate the number of words
    word_count = len(text.split())
    
    # Return the word count as a JSON response
    return {"word_count": word_count}

if __name__ == '__main__':
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
