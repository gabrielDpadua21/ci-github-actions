FROM python:latest

WORKDIR /app

COPY . .

CMD [ "python", "math.py" ]