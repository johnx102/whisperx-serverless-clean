#!/bin/bash
echo "[+] Initialisation du projet WhisperX Serverless..."

echo "[⚠️] Cette version nécessite que tu pushes ce dossier sur GitHub puis connectes-le à RunPod Serverless manuellement."
echo "[💡] Astuce : crée un dépôt GitHub, push ce dossier, puis choisis 'Deploy from GitHub' dans RunPod."

echo "[✅] Étapes restantes :"
echo "1. Remplace HF_TOKEN dans Dockerfile par ton token Hugging Face"
echo "2. Crée un repo GitHub (public ou privé)"
echo "3. Push :"
echo "   git init && git add . && git commit -m 'init' && git remote add origin <ton-repo> && git push -u origin master"
echo "4. Va sur https://runpod.io/ > Serverless > Deploy from GitHub"