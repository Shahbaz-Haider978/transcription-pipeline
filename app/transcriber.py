import whisper
from app.utils import convert_to_wav, split_audio

model = whisper.load_model("base")


def transcribe_file(file_path):
    wav_path = convert_to_wav(file_path)

    chunks = split_audio(wav_path)
    all_segments = []

    for chunk_path, offset in chunks:
        result = model.transcribe(chunk_path)

        for seg in result["segments"]:
            all_segments.append({
                "start": seg["start"] + offset,
                "end": seg["end"] + offset,
                "text": seg["text"]
            })

    return all_segments
