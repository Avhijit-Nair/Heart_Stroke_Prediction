# base image

FROM python:3.8

EXPOSE 8501
WORKDIR /docker_image_strokePredictionApp
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run heart_stroke_prediction_app.py