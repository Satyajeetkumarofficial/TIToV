from fastapi import FastAPI, File, UploadFile, Form
from generator import text_to_video, text_to_image, estimate_time
import time

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Text to Video Bot Running!"}

@app.post("/txt2video")
async def txt2video(text: str = Form(...)):
    start = time.time()
    output_video = text_to_video(text)
    return {
        "message": "Video created",
        "duration_sec": round(time.time() - start, 2),
        "file": output_video
    }

@app.post("/txt2image")
async def txt2image(text: str = Form(...)):
    output_image = text_to_image(text)
    return {"file": output_image}
