FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git ffmpeg wget curl python3-pip python3-dev libsndfile1 && apt-get clean

RUN pip3 install --upgrade pip setuptools

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

ENV HF_TOKEN=hf_YourHuggingFaceTokenHere

CMD ["python3", "runpod_handler.py"]