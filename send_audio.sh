#!/bin/bash

FILE="test.wav"
ENDPOINT="https://YOUR-RUNPOD-ENDPOINT/run"

echo "[+] Encodage du fichier $FILE"
ENCODED=$(base64 < "$FILE" | tr -d '\n')

echo "[+] Envoi à l'API RunPod..."
curl -X POST "$ENDPOINT"   -H "Content-Type: application/json"   -d '{"input": {"audio_base64": "'"$ENCODED"'"}}' | jq .