from pydub import AudioSegment

def convert_to_wav(input_path):
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)

    output_path = input_path + ".wav"
    audio.export(output_path, format="wav")

    return output_path


def split_audio(audio_path, chunk_ms=30000):
    audio = AudioSegment.from_wav(audio_path)
    chunks = []

    for i in range(0, len(audio), chunk_ms):
        chunk = audio[i:i + chunk_ms]
        chunk_path = f"{audio_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format="wav")
        chunks.append((chunk_path, i / 1000))  # offset in seconds

    return chunks
