FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 9000

WORKDIR /app/src
CMD ["gunicorn", "--bind", "0.0.0.0:9000", "Server:app"]