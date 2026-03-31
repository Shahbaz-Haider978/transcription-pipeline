from fastapi import FastAPI, UploadFile
import shutil
import uuid
from app.transcriber import transcribe_file

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Transcription API running"}


@app.post("/transcribe")
async def transcribe_audio(file: UploadFile):
    file_id = str(uuid.uuid4())
    file_path = f"temp_{file_id}_{file.filename}"

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe
    segments = transcribe_file(file_path)

    return {
        "file": file.filename,
        "segments": segments
    }
