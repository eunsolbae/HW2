from fastapi import FastAPI, UploadFile, File
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI 퍼스널 컬러 큐레이터가 작동 중입니다!"}

@app.post("/analyze-vibe")
async def analyze_vibe(file: UploadFile = File(...)):
    results = [
        {"color": "여름 쿨톤", "mood": "세련된 도시적 무드"},
        {"color": "봄 웜톤", "mood": "밝고 에너제틱한 무드"},
        {"color": "가을 웜톤", "mood": "차분하고 따뜻한 우디 무드"},
        {"color": "겨울 쿨톤", "mood": "카리스마 넘치는 모던 무드"}
    ]
    analysis = random.choice(results)
    return {"filename": file.filename, **analysis}
