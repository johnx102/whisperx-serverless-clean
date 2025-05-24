import whisperx
import torch
import os
import tempfile
import base64

# Chargement des modèles dès le démarrage
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisperx.load_model("large-v2", device)
model_a, metadata = whisperx.load_align_model(language_code="fr", device=device)
diarize_model = whisperx.DiarizationPipeline(use_auth_token=os.getenv("HF_TOKEN"), device=device)

def handler(event):
    try:
        # Extraction du fichier base64
        audio_base64 = event["input"]["audio_base64"]
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_audio.write(base64.b64decode(audio_base64))
            temp_audio_path = temp_audio.name

        # Étape 1 : transcription
        result = model.transcribe(temp_audio_path)

        # Étape 2 : alignement
        aligned = whisperx.align(result["segments"], model_a, metadata, temp_audio_path, device)

        # Étape 3 : diarisation
        diarize_segments = diarize_model(temp_audio_path)

        # Fusion
        final_segments = whisperx.merge_text_diarization(aligned["segments"], diarize_segments)

        return {
            "text": result["text"],
            "segments": final_segments
        }

    except Exception as e:
        return {"error": str(e)}
