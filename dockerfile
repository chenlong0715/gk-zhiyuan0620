FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
  && pip install --no-cache-dir pandas flask

EXPOSE 5000
CMD ["python", "app.py"]
