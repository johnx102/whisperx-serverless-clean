from flask import Flask, request, jsonify
import whisperx
import torch
import tempfile
import base64
import os

app = Flask(__name__)

# Chargement du modèle
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisperx.load_model("large-v2", device)
model_a, metadata = whisperx.load_align_model(language_code="fr", device=device)
diarize_model = whisperx.DiarizationPipeline(use_auth_token=os.getenv("HF_TOKEN"), device=device)

@app.route("/run", methods=["POST"])
def transcribe():
    try:
        data = request.json
        audio_base64 = data["input"]["audio_base64"]
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_audio.write(base64.b64decode(audio_base64))
            temp_audio_path = temp_audio.name

        result = model.transcribe(temp_audio_path)
        aligned = whisperx.align(result["segments"], model_a, metadata, temp_audio_path, device)
        diarize_segments = diarize_model(temp_audio_path)
        final = whisperx.merge_text_diarization(aligned["segments"], diarize_segments)

        return jsonify({
            "text": result["text"],
            "segments": final
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500