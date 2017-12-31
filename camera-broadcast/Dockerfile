FROM python:3.4-alpine
WORKDIR /src
RUN pip install -r requirements.txt
COPY * .
CMD ["python", "camerabroadcast.py"]