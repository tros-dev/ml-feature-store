from fastapi import FastAPI, HTTPException
from model import get_user_features

app = FastAPI()

@app.get("/features/{user_id}")
async def serve_features(user_id: int):
    features = get_user_features(user_id)
    if not features:
        raise HTTPException(status_code=404, detail="User features not found")
    return features
